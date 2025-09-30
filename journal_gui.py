import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import re
from database import JournalDatabase

class JournalGUI:
    def __init__(self):
        self.db = JournalDatabase()
        self.access_password = "1310"
        self.authenticated = False
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Personal Journal System - Premium Edition")
        self.root.geometry("1400x900")
        self.root.configure(bg="#f3f4f6")
        self.root.minsize(1000, 700)
        
        # Center window on screen
        self.center_window()
        
        # Simple color scheme - Clean theme with black text
        self.colors = {
            'primary': '#3b82f6',          # Blue
            'primary_dark': '#2563eb',     # Darker blue
            'primary_light': '#60a5fa',    # Light blue
            'secondary': '#10b981',        # Green
            'accent': '#f59e0b',           # Orange accent
            'background': '#f3f4f6',       # Light gray background
            'surface': '#ffffff',          # White card background
            'surface_variant': '#f9fafb',  # Light gray surface
            'on_surface': '#000000',       # Black text on white surface
            'on_background': '#000000',    # Black text on light background
            'border': '#e5e7eb',           # Light border
            'border_light': '#d1d5db',     # Lighter border
            'success': '#10b981',          # Success green
            'warning': '#f59e0b',          # Warning amber
            'error': '#ef4444',            # Error red
            'shadow': 'rgba(0, 0, 0, 0.1)', # Light shadow
            'gradient_start': '#3b82f6',   # Blue gradient start
            'gradient_end': '#8b5cf6'      # Purple gradient end
        }
        
        # Configure premium styles
        self.setup_premium_styles()
        
        # Show access screen first
        self.show_access_screen()
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        pos_x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        pos_y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
    
    def setup_premium_styles(self):
        """Setup premium custom styles for the application"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure premium styles with modern typography
        style.configure('Title.TLabel', 
                       font=('Arial', 32, 'bold'), 
                       background=self.colors['background'], 
                       foreground=self.colors['on_background'])
        
        style.configure('Heading.TLabel', 
                       font=('Arial', 18, 'bold'), 
                       background=self.colors['surface'], 
                       foreground=self.colors['on_surface'])
        
        style.configure('Body.TLabel', 
                       font=('Arial', 12), 
                       background=self.colors['surface'], 
                       foreground=self.colors['on_surface'])
    
    def clear_window(self):
        """Clear all widgets from the main window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def create_premium_button(self, parent, text, command, bg_color=None, fg_color='black', 
                             width=200, height=45, font_size=12, font_weight='normal'):
        """Create a premium styled button with hover effects"""
        if bg_color is None:
            bg_color = self.colors['primary']
        
        button_frame = tk.Frame(parent, bg=parent['bg'])
        
        def on_enter(event):
            button.configure(bg=self.colors['primary_light'], 
                           cursor="hand2")
        
        def on_leave(event):
            button.configure(bg=bg_color, cursor="")
        
        button = tk.Button(button_frame, text=text, command=command,
                          bg=bg_color, fg=fg_color, relief='flat',
                          font=('Arial', font_size, font_weight),
                          width=int(width/8), height=int(height/20),
                          borderwidth=0, cursor="hand2")
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.pack()
        
        return button_frame
    
    def show_access_screen(self):
        """Show premium password access screen"""
        self.clear_window()
        
        # Create main gradient background
        main_frame = tk.Frame(self.root, bg=self.colors['background'])
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Center container with glassmorphism effect
        center_frame = tk.Frame(main_frame, bg=self.colors['surface'], padx=50, pady=50,
                               relief='solid', borderwidth=2)
        center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Premium title
        title_label = tk.Label(center_frame, text="Personal Journal", 
                              font=('Arial', 36, 'bold'), 
                              fg=self.colors['primary'], bg=self.colors['surface'])
        title_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(center_frame, text="Premium Edition", 
                                 font=('Arial', 14), 
                                 fg=self.colors['accent'], bg=self.colors['surface'])
        subtitle_label.pack()
        
        # Elegant divider
        divider = tk.Frame(center_frame, bg=self.colors['border'], height=1)
        divider.pack(fill=tk.X, pady=20)
        
        # Access message
        access_label = tk.Label(center_frame, text="Enter your access credentials", 
                               font=('Arial', 16), 
                               fg=self.colors['on_surface'], bg=self.colors['surface'])
        access_label.pack(pady=(0, 30))
        
        # Password input
        password_label = tk.Label(center_frame, text="Access Code:", 
                                 font=('Arial', 12, 'bold'), 
                                 fg=self.colors['on_surface'], bg=self.colors['surface'])
        password_label.pack(anchor=tk.W, pady=(0, 8))
        
        # Entry with border
        entry_frame = tk.Frame(center_frame, bg=self.colors['surface_variant'], 
                              relief='solid', padx=2, pady=2, borderwidth=1)
        entry_frame.pack(fill=tk.X, pady=(0, 30))
        
        self.password_entry = tk.Entry(entry_frame, font=('Arial', 16), 
                                     width=25, show="●", relief='flat',
                                     bg=self.colors['surface_variant'], 
                                     fg=self.colors['on_surface'],
                                     insertbackground=self.colors['primary'],
                                     borderwidth=0, justify='center')
        self.password_entry.pack(pady=12, padx=15)
        self.password_entry.bind('<Return>', lambda e: self.check_password())
        
        # Login button
        login_btn_frame = self.create_premium_button(
            center_frame, "Enter Journal", self.check_password,
            bg_color=self.colors['primary'], width=250, height=50, font_size=14, fg_color='white'
        )
        login_btn_frame.pack(pady=(0, 30))
        
        # Feature highlights
        features_frame = tk.Frame(center_frame, bg=self.colors['surface_variant'], 
                                 padx=25, pady=20, relief='solid', borderwidth=1)
        features_frame.pack(fill=tk.X, pady=(0, 20))
        
        features_title = tk.Label(features_frame, text="✨ Premium Features", 
                                 font=('Arial', 14, 'bold'), 
                                 fg=self.colors['secondary'], bg=self.colors['surface_variant'])
        features_title.pack()
        
        features_list = [
            "🔒 Advanced Security & Privacy",
            "📝 Rich Text Editing Experience", 
            "🔍 Intelligent Search & Filtering",
            "💾 Auto-save & Backup Protection",
            "🎨 Beautiful Premium Interface"
        ]
        
        for feature in features_list:
            feature_label = tk.Label(features_frame, text=feature, 
                                   font=('Arial', 11), 
                                   fg=self.colors['on_surface'], 
                                   bg=self.colors['surface_variant'],
                                   anchor='w')
            feature_label.pack(fill=tk.X, pady=2)
        
        # Credits
        credits_label = tk.Label(center_frame, 
                                text="Developed by ST AIML-B Team: Ayush Kumawat (12) • Nikita Mishra (24) • Satyam Mishra (25)", 
                                font=('Arial', 9), 
                                fg=self.colors['border'], 
                                bg=self.colors['surface'])
        credits_label.pack(pady=(20, 0))
        
        self.password_entry.focus()
    
    def check_password(self):
        """Check if entered password is correct"""
        if self.password_entry.get() == self.access_password:
            self.authenticated = True
            self.show_dashboard()
        else:
            messagebox.showerror("Access Denied", 
                               "Invalid access code. Please try again.",
                               icon='error')
            self.password_entry.delete(0, tk.END)
    
    def show_dashboard(self):
        """Show premium main dashboard"""
        self.clear_window()
        
        # Create main container with dark theme
        main_container = tk.Frame(self.root, bg=self.colors['background'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Header
        header_frame = tk.Frame(main_container, bg=self.colors['background'], 
                               padx=30, pady=20)
        header_frame.pack(fill=tk.X, pady=(0, 25))
        
        # Title section
        title_label = tk.Label(header_frame, text="Journal Dashboard", 
                              font=('Arial', 28, 'bold'), 
                              fg=self.colors['on_background'], bg=self.colors['background'])
        title_label.pack(side=tk.LEFT, anchor=tk.W)
        
        # Action buttons
        actions_frame = tk.Frame(header_frame, bg=self.colors['background'])
        actions_frame.pack(side=tk.RIGHT)
        
        new_btn_frame = self.create_premium_button(
            actions_frame, "✏️ New Entry", self.show_create_entry,
            bg_color=self.colors['primary'], width=180, height=45, font_size=12, fg_color='white'
        )
        new_btn_frame.pack(side=tk.LEFT, padx=(0, 15))
        
        logout_btn_frame = self.create_premium_button(
            actions_frame, "↗️ Logout", self.logout,
            bg_color=self.colors['border_light'], width=120, height=45, font_size=12
        )
        logout_btn_frame.pack(side=tk.LEFT)
        
        # Statistics section
        stats_container = tk.Frame(main_container, bg=self.colors['background'])
        stats_container.pack(fill=tk.X, pady=(0, 25))
        
        total_entries = self.db.get_entry_count()
        
        # Stats cards
        stats_row = tk.Frame(stats_container, bg=self.colors['background'])
        stats_row.pack(fill=tk.X)
        
        # Total entries card
        entries_card = tk.Frame(stats_row, bg=self.colors['surface'], 
                               padx=25, pady=20, relief='solid', borderwidth=1)
        entries_card.pack(side=tk.LEFT, padx=(0, 20), fill=tk.BOTH, expand=True)
        
        entries_icon = tk.Label(entries_card, text="📊", font=('Arial', 24), 
                               bg=self.colors['surface'])
        entries_icon.pack()
        
        entries_number = tk.Label(entries_card, text=str(total_entries), 
                                 font=('Arial', 32, 'bold'), 
                                 fg=self.colors['primary'], bg=self.colors['surface'])
        entries_number.pack()
        
        entries_label = tk.Label(entries_card, text="Total Entries", 
                                font=('Arial', 12, 'bold'), 
                                fg=self.colors['on_surface'], bg=self.colors['surface'])
        entries_label.pack()
        
        # Status card
        status_card = tk.Frame(stats_row, bg=self.colors['surface'], 
                              padx=25, pady=20, relief='solid', borderwidth=1)
        status_card.pack(side=tk.LEFT, padx=(0, 20), fill=tk.BOTH, expand=True)
        
        status_icon = tk.Label(status_card, text="⚡", font=('Arial', 24), 
                              bg=self.colors['surface'])
        status_icon.pack()
        
        status_text = tk.Label(status_card, text="Active", 
                              font=('Arial', 18, 'bold'), 
                              fg=self.colors['success'], bg=self.colors['surface'])
        status_text.pack()
        
        status_label = tk.Label(status_card, text="Status", 
                               font=('Arial', 12, 'bold'), 
                               fg=self.colors['on_surface'], bg=self.colors['surface'])
        status_label.pack()
        
        # Storage card
        storage_card = tk.Frame(stats_row, bg=self.colors['surface'], 
                               padx=25, pady=20, relief='solid', borderwidth=1)
        storage_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        storage_icon = tk.Label(storage_card, text="💾", font=('Arial', 24), 
                               bg=self.colors['surface'])
        storage_icon.pack()
        
        storage_text = tk.Label(storage_card, text="Local", 
                               font=('Arial', 18, 'bold'), 
                               fg=self.colors['accent'], bg=self.colors['surface'])
        storage_text.pack()
        
        storage_label = tk.Label(storage_card, text="Storage", 
                                font=('Arial', 12, 'bold'), 
                                fg=self.colors['on_surface'], bg=self.colors['surface'])
        storage_label.pack()
        
        # Search section
        search_frame = tk.Frame(main_container, bg=self.colors['surface'], 
                               padx=25, pady=20, relief='solid', borderwidth=1)
        search_frame.pack(fill=tk.X, pady=(0, 20))
        
        search_label = tk.Label(search_frame, text="🔍 Search Entries", 
                               font=('Arial', 16, 'bold'), 
                               fg=self.colors['on_surface'], bg=self.colors['surface'])
        search_label.pack(side=tk.LEFT)
        
        # Search entry
        search_container = tk.Frame(search_frame, bg=self.colors['surface_variant'], 
                                   relief='solid', padx=3, pady=3, borderwidth=1)
        search_container.pack(side=tk.RIGHT, padx=(20, 0))
        
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.filter_entries)
        
        self.search_entry = tk.Entry(search_container, textvariable=self.search_var,
                                    font=('Arial', 12), width=30, relief='flat',
                                    bg=self.colors['surface_variant'], 
                                    fg=self.colors['on_surface'],
                                    insertbackground=self.colors['primary'],
                                    borderwidth=0)
        self.search_entry.pack(pady=8, padx=12)
        
        # Entries section
        entries_section = tk.Frame(main_container, bg=self.colors['background'])
        entries_section.pack(fill=tk.BOTH, expand=True)
        
        # Section header
        entries_title = tk.Label(entries_section, text="📝 Your Entries", 
                                font=('Arial', 18, 'bold'), 
                                fg=self.colors['on_background'], bg=self.colors['background'])
        entries_title.pack(anchor=tk.W, pady=(0, 15))
        
        # Scrollable entries container
        canvas_frame = tk.Frame(entries_section, bg=self.colors['background'])
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        self.entries_canvas = tk.Canvas(canvas_frame, bg=self.colors['background'], 
                                       highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=self.entries_canvas.yview)
        self.scrollable_frame = tk.Frame(self.entries_canvas, bg=self.colors['background'])
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.entries_canvas.configure(scrollregion=self.entries_canvas.bbox("all"))
        )
        
        self.entries_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.entries_canvas.configure(yscrollcommand=scrollbar.set)
        
        self.entries_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Mouse wheel binding
        def _on_mousewheel(event):
            self.entries_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.entries_canvas.bind("<MouseWheel>", _on_mousewheel)
        
        # Load entries
        self.load_entries()
    
    def load_entries(self):
        """Load and display entries"""
        # Clear existing entries
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        # Get entries
        search_query = getattr(self, 'search_var', tk.StringVar()).get().strip()
        if search_query:
            entries = self.db.search_entries(search_query)
        else:
            entries = self.db.get_all_entries()
        
        if not entries:
            # No entries message
            no_entries_frame = tk.Frame(self.scrollable_frame, bg=self.colors['surface'],
                                       padx=40, pady=40, relief='solid', borderwidth=1)
            no_entries_frame.pack(fill=tk.X, pady=20)
            
            no_entries_icon = tk.Label(no_entries_frame, text="📝", 
                                      font=('Arial', 48), 
                                      bg=self.colors['surface'])
            no_entries_icon.pack()
            
            no_entries_title = tk.Label(no_entries_frame, text="No entries yet", 
                                       font=('Arial', 24, 'bold'), 
                                       fg=self.colors['on_surface'], bg=self.colors['surface'])
            no_entries_title.pack(pady=(10, 5))
            
            no_entries_text = tk.Label(no_entries_frame, 
                                      text="Start your journaling journey by creating your first entry.", 
                                      font=('Arial', 14), 
                                      fg=self.colors['border_light'], bg=self.colors['surface'])
            no_entries_text.pack()
            
            # Create first entry button
            first_entry_btn = self.create_premium_button(
                no_entries_frame, "✨ Create First Entry", self.show_create_entry,
                bg_color=self.colors['primary'], width=200, height=40, font_size=12, fg_color='white'
            )
            first_entry_btn.pack(pady=(20, 0))
        else:
            for entry in entries:
                self.create_premium_entry_card(entry)
    
    def create_premium_entry_card(self, entry):
        """Create a premium styled entry card"""
        # Main entry card
        card_container = tk.Frame(self.scrollable_frame, bg=self.colors['background'])
        card_container.pack(fill=tk.X, pady=(0, 15))
        
        entry_card = tk.Frame(card_container, bg=self.colors['surface'], 
                             padx=25, pady=20, relief='solid', borderwidth=1)
        entry_card.pack(fill=tk.X, padx=5)
        
        # Card header
        header_frame = tk.Frame(entry_card, bg=self.colors['surface'])
        header_frame.pack(fill=tk.X, pady=(0, 12))
        
        # Title
        title_label = tk.Label(header_frame, text=entry[1], 
                              font=('Arial', 18, 'bold'), 
                              fg=self.colors['primary'], bg=self.colors['surface'],
                              cursor="hand2")
        title_label.pack(side=tk.LEFT, anchor=tk.W)
        title_label.bind("<Button-1>", lambda e: self.view_entry(entry[0]))
        
        # Date
        date_str = datetime.fromisoformat(entry[3]).strftime("%B %d, %Y • %I:%M %p")
        date_label = tk.Label(header_frame, text=date_str, 
                             font=('Arial', 11), 
                             fg=self.colors['border_light'], bg=self.colors['surface'])
        date_label.pack(side=tk.RIGHT)
        
        # Content preview
        clean_content = self.clean_content_preview(entry[2])
        if clean_content:
            content_label = tk.Label(entry_card, text=clean_content, 
                                   font=('Arial', 12), 
                                   fg=self.colors['on_surface'], bg=self.colors['surface'],
                                   justify=tk.LEFT, anchor="w", wraplength=800)
            content_label.pack(fill=tk.X, pady=(0, 15))
        
        # Action buttons
        actions_frame = tk.Frame(entry_card, bg=self.colors['surface'])
        actions_frame.pack(fill=tk.X)
        
        view_btn_frame = self.create_premium_button(
            actions_frame, "👁️ View", lambda: self.view_entry(entry[0]),
            bg_color=self.colors['secondary'], width=100, height=35, font_size=10, fg_color='white'
        )
        view_btn_frame.pack(side=tk.LEFT, padx=(0, 10))
        
        edit_btn_frame = self.create_premium_button(
            actions_frame, "✏️ Edit", lambda: self.show_edit_entry(entry[0]),
            bg_color=self.colors['warning'], width=100, height=35, font_size=10, fg_color='white'
        )
        edit_btn_frame.pack(side=tk.LEFT, padx=(0, 10))
        
        delete_btn_frame = self.create_premium_button(
            actions_frame, "🗑️ Delete", lambda: self.delete_entry_with_confirmation(entry[0]),
            bg_color=self.colors['error'], width=100, height=35, font_size=10, fg_color='white'
        )
        delete_btn_frame.pack(side=tk.LEFT)
        
        # Hover effect
        def on_card_enter(event):
            entry_card.configure(relief='solid', borderwidth=2)
        
        def on_card_leave(event):
            entry_card.configure(relief='solid', borderwidth=1)
        
        entry_card.bind("<Enter>", on_card_enter)
        entry_card.bind("<Leave>", on_card_leave)
    
    def filter_entries(self, *args):
        """Filter entries based on search query"""
        self.load_entries()
    
    def clean_content_preview(self, content):
        """Clean content for preview"""
        if not content:
            return ""
        
        # Remove HTML tags
        clean_text = re.sub('<.*?>', '', content)
        
        # Remove extra whitespace
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        
        return clean_text[:150] + "..." if len(clean_text) > 150 else clean_text
    
    def delete_entry_with_confirmation(self, entry_id):
        """Delete an entry with confirmation"""
        result = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this entry?")
        if result:
            try:
                self.db.delete_entry(entry_id)
                messagebox.showinfo("Success", "Entry deleted successfully!")
                self.load_entries()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete entry: {str(e)}")
    
    def show_create_entry(self):
        """Show create entry form"""
        self.show_entry_form("Create New Entry", "", "")
    
    def show_edit_entry(self, entry_id):
        """Show edit entry form"""
        entry = self.db.get_entry_by_id(entry_id)
        if entry:
            self.show_entry_form("Edit Entry", entry[1], entry[2], entry_id)
    
    def view_entry(self, entry_id):
        """Show view entry window"""
        entry = self.db.get_entry_by_id(entry_id)
        if not entry:
            messagebox.showerror("Error", "Entry not found!")
            return
        
        entry_id, title, content, created_at, updated_at = entry
        
        view_window = tk.Toplevel(self.root)
        view_window.title(f"View: {title}")
        view_window.geometry("900x700")
        view_window.configure(bg=self.colors['background'])
        view_window.transient(self.root)
        view_window.grab_set()
        
        # Main container
        main_frame = tk.Frame(view_window, bg=self.colors['background'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_frame = tk.Frame(main_frame, bg=self.colors['primary'], padx=30, pady=20)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(header_frame, text=title, font=('Arial', 24, 'bold'), 
                              fg="white", bg=self.colors['primary'])
        title_label.pack(anchor=tk.W)
        
        created_date = datetime.fromisoformat(created_at).strftime('%B %d, %Y at %I:%M %p')
        date_label = tk.Label(header_frame, text=f"Created: {created_date}", 
                             font=('Arial', 12), fg="white", bg=self.colors['primary'])
        date_label.pack(anchor=tk.W, pady=(5, 0))
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg=self.colors['surface'], 
                                relief="solid", borderwidth=1, padx=30, pady=30)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Content text
        text_frame = tk.Frame(content_frame, bg=self.colors['surface'])
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        content_display = tk.Text(text_frame, font=('Arial', 12), wrap=tk.WORD, 
                                 relief="flat", borderwidth=0, state=tk.DISABLED,
                                 bg=self.colors['surface'], fg=self.colors['on_surface'])
        content_scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=content_display.yview)
        content_display.configure(yscrollcommand=content_scrollbar.set)
        
        content_display.config(state=tk.NORMAL)
        content_display.insert(1.0, content)
        content_display.config(state=tk.DISABLED)
        
        content_display.pack(side="left", fill="both", expand=True)
        content_scrollbar.pack(side="right", fill="y")
        
        # Buttons
        buttons_frame = tk.Frame(content_frame, bg=self.colors['surface'])
        buttons_frame.pack(fill=tk.X)
        
        back_btn_frame = self.create_premium_button(
            buttons_frame, "← Back", view_window.destroy,
            bg_color=self.colors['border_light'], width=120, height=40, font_size=11
        )
        back_btn_frame.pack(side=tk.LEFT)
        
        edit_btn_frame = self.create_premium_button(
            buttons_frame, "✏️ Edit", lambda: [view_window.destroy(), self.show_edit_entry(entry_id)],
            bg_color=self.colors['warning'], width=120, height=40, font_size=11, fg_color='white'
        )
        edit_btn_frame.pack(side=tk.RIGHT, padx=(10, 0))
        
        delete_btn_frame = self.create_premium_button(
            buttons_frame, "🗑️ Delete", lambda: [view_window.destroy(), self.delete_entry_with_confirmation(entry_id)],
            bg_color=self.colors['error'], width=120, height=40, font_size=11, fg_color='white'
        )
        delete_btn_frame.pack(side=tk.RIGHT)
    
    def show_entry_form(self, window_title, title="", content="", entry_id=None):
        """Show entry form window"""
        form_window = tk.Toplevel(self.root)
        form_window.title(window_title)
        form_window.geometry("900x700")
        form_window.configure(bg=self.colors['background'])
        form_window.transient(self.root)
        form_window.grab_set()
        
        # Main container
        main_frame = tk.Frame(form_window, bg=self.colors['background'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, text=window_title, font=('Arial', 20, 'bold'), 
                              fg=self.colors['on_background'], bg=self.colors['background'])
        title_label.pack(pady=(0, 20))
        
        # Form frame
        form_frame = tk.Frame(main_frame, bg=self.colors['surface'], 
                             relief="solid", borderwidth=1, padx=30, pady=30)
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title field
        title_label = tk.Label(form_frame, text="Title:", font=('Arial', 12, 'bold'), 
                              fg=self.colors['on_surface'], bg=self.colors['surface'])
        title_label.pack(anchor=tk.W, pady=(0, 5))
        
        title_entry = tk.Entry(form_frame, font=('Arial', 14), width=80,
                              bg=self.colors['surface_variant'], fg=self.colors['on_surface'],
                              relief="solid", borderwidth=1)
        title_entry.pack(fill=tk.X, pady=(0, 20))
        title_entry.insert(0, title)
        
        # Content field
        content_label = tk.Label(form_frame, text="Content:", font=('Arial', 12, 'bold'), 
                                 fg=self.colors['on_surface'], bg=self.colors['surface'])
        content_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Text widget
        text_frame = tk.Frame(form_frame, bg=self.colors['surface'])
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        content_text = tk.Text(text_frame, font=('Arial', 12), wrap=tk.WORD, 
                              relief="solid", borderwidth=1,
                              bg=self.colors['surface_variant'], fg=self.colors['on_surface'])
        content_scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=content_text.yview)
        content_text.configure(yscrollcommand=content_scrollbar.set)
        
        content_text.pack(side="left", fill="both", expand=True)
        content_scrollbar.pack(side="right", fill="y")
        
        content_text.insert(1.0, content)
        
        # Buttons
        buttons_frame = tk.Frame(form_frame, bg=self.colors['surface'])
        buttons_frame.pack(fill=tk.X, pady=(10, 0))
        
        cancel_btn_frame = self.create_premium_button(
            buttons_frame, "Cancel", form_window.destroy,
            bg_color=self.colors['border_light'], width=120, height=40, font_size=11
        )
        cancel_btn_frame.pack(side=tk.LEFT)
        
        save_btn_frame = self.create_premium_button(
            buttons_frame, "💾 Save Entry", lambda: self.save_entry(form_window, title_entry, content_text, entry_id),
            bg_color=self.colors['primary'], width=150, height=40, font_size=11, fg_color='white'
        )
        save_btn_frame.pack(side=tk.RIGHT)
        
        title_entry.focus()
    
    def save_entry(self, window, title_entry, content_text, entry_id=None):
        """Save entry"""
        title = title_entry.get().strip()
        content = content_text.get(1.0, tk.END).strip()
        
        if not title:
            messagebox.showerror("Error", "Title is required!")
            return
        
        if not content:
            messagebox.showerror("Error", "Content is required!")
            return
        
        try:
            if entry_id:
                self.db.update_entry(entry_id, title, content)
                messagebox.showinfo("Success", "Entry updated successfully!")
            else:
                self.db.create_entry(title, content)
                messagebox.showinfo("Success", "Entry created successfully!")
            
            window.destroy()
            self.load_entries()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save entry: {str(e)}")
    
    def logout(self):
        """Logout and return to access screen"""
        self.authenticated = False
        self.show_access_screen()
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = JournalGUI()
    app.run()
