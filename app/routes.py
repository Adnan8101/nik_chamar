import re
from flask import Blueprint, render_template, redirect, url_for, flash, request, session, current_app
from app import db
from app.models import JournalEntry
from app.forms import AccessForm, JournalEntryForm
from datetime import datetime

bp = Blueprint('main', __name__)

def clean_html_content(html_content):
    """Clean HTML content and extract plain text for preview"""
    if not html_content:
        return ""
    
    # Remove HTML tags
    clean_text = re.sub('<.*?>', '', html_content)
    
    # Remove extra whitespace and newlines
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    # Remove any remaining encoded characters or session tokens
    clean_text = re.sub(r'[A-Za-z0-9+/=]{50,}', '', clean_text)  # Remove long encoded strings
    clean_text = re.sub(r'\.[\w\-_]{20,}', '', clean_text)  # Remove session-like tokens
    
    return clean_text

def require_access():
    """Check if user has entered correct password"""
    if not session.get('access_granted'):
        return redirect(url_for('main.access'))
    return None

@bp.route('/')
def index():
    """Home page - redirects to access or dashboard"""
    if not session.get('access_granted'):
        return redirect(url_for('main.access'))
    return redirect(url_for('main.dashboard'))

@bp.route('/access', methods=['GET', 'POST'])
def access():
    """Access page with password protection"""
    if session.get('access_granted'):
        return redirect(url_for('main.dashboard'))
    
    form = AccessForm()
    if form.validate_on_submit():
        if form.password.data == current_app.config['ACCESS_PASSWORD']:
            session['access_granted'] = True
            session.permanent = True
            flash('Access granted! Welcome to your Personal Journal.', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid password. Please try again.', 'danger')
    
    return render_template('access.html', form=form)

@bp.route('/dashboard')
def dashboard():
    """Main journal dashboard"""
    access_check = require_access()
    if access_check:
        return access_check
    
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '')
    
    # Base query for all entries
    query = JournalEntry.query
    
    # Apply search filter if provided
    if search_query:
        query = query.filter(
            JournalEntry.title.contains(search_query) |
            JournalEntry.content.contains(search_query)
        )
    
    # Paginate results
    entries = query.order_by(JournalEntry.created_at.desc()).paginate(
        page=page, per_page=10, error_out=False
    )
    
    # Clean the content for each entry for preview
    for entry in entries.items:
        entry.clean_preview = clean_html_content(entry.content)[:200]
    
    # Get total count
    total_entries = JournalEntry.query.count()
    
    return render_template('dashboard.html',
                         entries=entries,
                         total_entries=total_entries,
                         current_search=search_query)

@bp.route('/create', methods=['GET', 'POST'])
def create_entry():
    """Create a new journal entry"""
    access_check = require_access()
    if access_check:
        return access_check
    
    form = JournalEntryForm()
    
    if form.validate_on_submit():
        entry = JournalEntry(
            title=form.title.data,
            content=form.content.data
        )
        
        db.session.add(entry)
        db.session.commit()
        flash('Journal entry created successfully!', 'success')
        return redirect(url_for('main.view_entry', id=entry.id))
    
    return render_template('create_entry.html', form=form)

@bp.route('/entry/<int:id>')
def view_entry(id):
    """View a specific journal entry"""
    access_check = require_access()
    if access_check:
        return access_check
    
    entry = JournalEntry.query.get_or_404(id)
    return render_template('view_entry.html', entry=entry)

@bp.route('/entry/<int:id>/edit', methods=['GET', 'POST'])
def edit_entry(id):
    """Edit a journal entry"""
    access_check = require_access()
    if access_check:
        return access_check
    
    entry = JournalEntry.query.get_or_404(id)
    form = JournalEntryForm()
    
    if form.validate_on_submit():
        entry.title = form.title.data
        entry.content = form.content.data
        entry.updated_at = datetime.utcnow()
        
        db.session.commit()
        flash('Journal entry updated successfully!', 'success')
        return redirect(url_for('main.view_entry', id=entry.id))
    
    elif request.method == 'GET':
        form.title.data = entry.title
        form.content.data = entry.content
    
    return render_template('edit_entry.html', form=form, entry=entry)

@bp.route('/entry/<int:id>/delete', methods=['POST'])
def delete_entry(id):
    """Delete a journal entry"""
    access_check = require_access()
    if access_check:
        return access_check
    
    entry = JournalEntry.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    flash('Journal entry deleted successfully.', 'info')
    return redirect(url_for('main.dashboard'))

@bp.route('/logout')
def logout():
    """Clear session and redirect to access page"""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.access'))
