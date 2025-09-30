import sqlite3
from datetime import datetime
import os

class JournalDatabase:
    def __init__(self, db_path="journal.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database and create tables if they don't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS journal_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_entry(self, title, content):
        """Create a new journal entry"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO journal_entries (title, content, created_at, updated_at)
            VALUES (?, ?, ?, ?)
        ''', (title, content, datetime.now(), datetime.now()))
        
        entry_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return entry_id
    
    def get_all_entries(self, search_query=None):
        """Get all journal entries, optionally filtered by search query"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if search_query:
            cursor.execute('''
                SELECT id, title, content, created_at, updated_at
                FROM journal_entries
                WHERE title LIKE ? OR content LIKE ?
                ORDER BY created_at DESC
            ''', (f'%{search_query}%', f'%{search_query}%'))
        else:
            cursor.execute('''
                SELECT id, title, content, created_at, updated_at
                FROM journal_entries
                ORDER BY created_at DESC
            ''')
        
        entries = cursor.fetchall()
        conn.close()
        return entries
    
    def get_entry_by_id(self, entry_id):
        """Get a specific journal entry by ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, content, created_at, updated_at
            FROM journal_entries
            WHERE id = ?
        ''', (entry_id,))
        
        entry = cursor.fetchone()
        conn.close()
        return entry
    
    def update_entry(self, entry_id, title, content):
        """Update an existing journal entry"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE journal_entries
            SET title = ?, content = ?, updated_at = ?
            WHERE id = ?
        ''', (title, content, datetime.now(), entry_id))
        
        conn.commit()
        conn.close()
    
    def delete_entry(self, entry_id):
        """Delete a journal entry"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM journal_entries WHERE id = ?', (entry_id,))
        
        conn.commit()
        conn.close()
    
    def get_entry_count(self):
        """Get total number of entries"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM journal_entries')
        count = cursor.fetchone()[0]
        
        conn.close()
        return count
