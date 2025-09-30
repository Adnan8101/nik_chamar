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
        self.root.title("Personal Journal System")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f8fafc")
        
        # Configure styles
        self.setup_styles()
        
        # Show access screen first
        self.show_access_screen()
    
    def setup_styles(self):
        """Setup custom styles for the application"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom styles
        style.configure('Title.TLabel', font=('Inter', 24, 'bold'), background="#f8fafc", foreground="#1f2937")
        style.configure('Heading.TLabel', font=('Inter', 16, 'bold'), background="#f8fafc", foreground="#374151")
        style.configure('Body.TLabel', font=('Inter', 11), background="#f8fafc", foreground="#6b7280")
        style.configure('Card.TFrame', background="#ffffff", relief="solid", borderwidth=1)
        style.configure('Primary.TButton', font=('Inter', 10, 'bold'))
        style.configure('Danger.TButton', font=('Inter', 10, 'bold'))
    
    def clear_window(self):
        """Clear all widgets from the main window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_access_screen(self):
        """Show password access screen"""
        self.clear_window()
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#667eea")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Center container
        center_frame = tk.Frame(main_frame, bg="#ffffff", padx=40, pady=40)
        center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Title
        title_label = tk.Label(center_frame, text="Personal Journal", 
                              font=('Inter', 28, 'bold'), fg="#1f2937", bg="#ffffff")
        title_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(center_frame, text="Enter password to access your journal", 
                                 font=('Inter', 14), fg="#6b7280", bg="#ffffff")
        subtitle_label.pack(pady=(0, 30))
        
        # Password entry
        password_label = tk.Label(center_frame, text="Access Password:", 
                                 font=('Inter', 12, 'bold'), fg="#374151", bg="#ffffff")
        password_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.password_entry = tk.Entry(center_frame, font=('Inter', 14), width=25, show="*")
        self.password_entry.pack(pady=(0, 20))
        self.password_entry.bind('<Return>', lambda e: self.check_password())
        
        # Login button
        login_btn = tk.Button(center_frame, text="Enter", font=('Inter', 12, 'bold'),
                             bg="#4f46e5", fg="white", padx=30, pady=10,
                             command=self.check_password, cursor="hand2")
        login_btn.pack(pady=(0, 20))
        
        # Info
        info_frame = tk.Frame(center_frame, bg="#eef2ff", padx=20, pady=15)
        info_frame.pack(fill=tk.X)
        
        info_title = tk.Label(info_frame, text="Simple & Secure", 
                             font=('Inter', 12, 'bold'), fg="#1f2937", bg="#eef2ff")
        info_title.pack()
        
        info_text = tk.Label(info_frame, text="Your personal space for thoughts, reflections, and memories.\nSimple CRUD operations with rich text editing.", 
                            font=('Inter', 10), fg="#6b7280", bg="#eef2ff", justify=tk.CENTER)
        info_text.pack(pady=(5, 0))
        
        # Credits
        credits_label = tk.Label(center_frame, text="Made by ST AIML-B | Ayush Kumawat (12) | Nikita Mishra (24) | Satyam Mishra (25)", 
                                font=('Inter', 9), fg="#9ca3af", bg="#ffffff")
        credits_label.pack(pady=(20, 0))
        
        self.password_entry.focus()
    
    def check_password(self):
        """Check if entered password is correct"""
        if self.password_entry.get() == self.access_password:
            self.authenticated = True
            self.show_dashboard()
        else:
            messagebox.showerror("Access Denied", "Invalid password. Please try again.")
            self.password_entry.delete(0, tk.END)
    
    def show_dashboard(self):
        """Show main dashboard"""
        self.clear_window()
        
        # Create main container
        main_container = tk.Frame(self.root, bg="#f8fafc")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_frame = tk.Frame(main_container, bg="#f8fafc")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(header_frame, text="Your Journal Dashboard", style='Title.TLabel')
        title_label.pack(side=tk.LEFT)
        
        # Buttons frame
        buttons_frame = tk.Frame(header_frame, bg="#f8fafc")
        buttons_frame.pack(side=tk.RIGHT)
        
        new_btn = tk.Button(buttons_frame, text="+ New Entry", font=('Inter', 11, 'bold'),
                           bg="#4f46e5", fg="white", padx=20, pady=8,
                           command=self.show_create_entry, cursor="hand2")
        new_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        logout_btn = tk.Button(buttons_frame, text="Logout", font=('Inter', 11),
                              bg="#6b7280", fg="white", padx=15, pady=8,
                              command=self.logout, cursor="hand2")
        logout_btn.pack(side=tk.LEFT)
        
        # Stats frame
        stats_frame = tk.Frame(main_container, bg="#f8fafc")
        stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        total_entries = self.db.get_entry_count()
        
        # Stats card
        stats_card = tk.Frame(stats_frame, bg="#ffffff", relief="solid", borderwidth=1)
        stats_card.pack(side=tk.LEFT, padx=(0, 15), pady=5, ipadx=20, ipady=15)
        
        stats_title = tk.Label(stats_card, text="Total Entries", font=('Inter', 12, 'bold'), 
                              fg="#6b7280", bg="#ffffff")
        stats_title.pack()
        
        stats_number = tk.Label(stats_card, text=str(total_entries), font=('Inter', 24, 'bold'), 
                               fg="#1f2937", bg="#ffffff")
        stats_number.pack()
        
        # Search frame
        search_frame = tk.Frame(main_container, bg="#ffffff", relief="solid", borderwidth=1)
        search_frame.pack(fill=tk.X, pady=(0, 20), padx=5, ipady=15)
        
        search_label = tk.Label(search_frame, text="Search:", font=('Inter', 12, 'bold'), 
                               fg="#374151", bg="#ffffff")
        search_label.pack(side=tk.LEFT, padx=(20, 10))
        
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, font=('Inter', 12), width=40)
        search_entry.pack(side=tk.LEFT, padx=(0, 10))
        search_entry.bind('<KeyRelease>', lambda e: self.update_entries_list())
        
        search_btn = tk.Button(search_frame, text="Search", font=('Inter', 11),
                              bg="#4f46e5", fg="white", padx=15, pady=5,
                              command=self.update_entries_list, cursor="hand2")
        search_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_btn = tk.Button(search_frame, text="Clear", font=('Inter', 11),
                             bg="#6b7280", fg="white", padx=15, pady=5,
                             command=self.clear_search, cursor="hand2")
        clear_btn.pack(side=tk.LEFT)
        
        # Entries frame with scrollbar
        entries_container = tk.Frame(main_container, bg="#f8fafc")
        entries_container.pack(fill=tk.BOTH, expand=True)
        
        # Canvas and scrollbar for entries
        canvas = tk.Canvas(entries_container, bg="#f8fafc")
        scrollbar = ttk.Scrollbar(entries_container, orient="vertical", command=canvas.yview)
        self.entries_frame = tk.Frame(canvas, bg="#f8fafc")
        
        self.entries_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.entries_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel to canvas
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind("<MouseWheel>", _on_mousewheel)
        
        # Load entries
        self.update_entries_list()
    
    def clear_search(self):
        """Clear search field and update entries"""
        self.search_var.set("")
        self.update_entries_list()
    
    def clean_content_preview(self, content):
        """Clean HTML content for preview"""
        if not content:
            return ""
        
        # Remove HTML tags
        clean_text = re.sub('<.*?>', '', content)
        
        # Remove extra whitespace and newlines
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        
        # Remove encoded characters or tokens
        clean_text = re.sub(r'[A-Za-z0-9+/=]{50,}', '', clean_text)
        clean_text = re.sub(r'\.[\w\-_]{20,}', '', clean_text)
        
        return clean_text[:150] + "..." if len(clean_text) > 150 else clean_text
    
    def update_entries_list(self):
        """Update the entries list display"""
        # Clear existing entries
        for widget in self.entries_frame.winfo_children():
            widget.destroy()
        
        # Get entries
        search_query = self.search_var.get().strip()
        entries = self.db.get_all_entries(search_query if search_query else None)
        
        if not entries:
            no_entries_label = tk.Label(self.entries_frame, text="No entries found" if search_query else "No entries yet. Create your first entry!", 
                                       font=('Inter', 14), fg="#6b7280", bg="#f8fafc")
            no_entries_label.pack(pady=50)
            return
        
        # Display entries
        for entry in entries:
            entry_id, title, content, created_at, updated_at = entry
            
            # Entry card
            entry_card = tk.Frame(self.entries_frame, bg="#ffffff", relief="solid", borderwidth=1)
            entry_card.pack(fill=tk.X, pady=(0, 15), padx=5)
            
            # Entry content frame
            content_frame = tk.Frame(entry_card, bg="#ffffff")
            content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
            
            # Title and date frame
            title_frame = tk.Frame(content_frame, bg="#ffffff")
            title_frame.pack(fill=tk.X, pady=(0, 10))
            
            title_label = tk.Label(title_frame, text=title, font=('Inter', 16, 'bold'), 
                                  fg="#1f2937", bg="#ffffff", cursor="hand2")
            title_label.pack(side=tk.LEFT)
            title_label.bind("<Button-1>", lambda e, eid=entry_id: self.show_view_entry(eid))
            
            # Date info
            created_date = datetime.fromisoformat(created_at.replace('Z', '+00:00')).strftime('%B %d, %Y at %I:%M %p')
            date_label = tk.Label(title_frame, text=created_date, font=('Inter', 10), 
                                 fg="#6b7280", bg="#ffffff")
            date_label.pack(side=tk.RIGHT)
            
            # Content preview
            preview_text = self.clean_content_preview(content)
            if preview_text:
                preview_frame = tk.Frame(content_frame, bg="#f9fafb", relief="solid", borderwidth=1)
                preview_frame.pack(fill=tk.X, pady=(0, 15), padx=5)
                
                preview_label = tk.Label(preview_frame, text=preview_text, font=('Inter', 11), 
                                       fg="#374151", bg="#f9fafb", wraplength=800, justify=tk.LEFT)
                preview_label.pack(padx=15, pady=10, anchor=tk.W)
            
            # Buttons frame
            buttons_frame = tk.Frame(content_frame, bg="#ffffff")
            buttons_frame.pack(fill=tk.X)
            
            view_btn = tk.Button(buttons_frame, text="View", font=('Inter', 10),
                                bg="#4f46e5", fg="white", padx=15, pady=5,
                                command=lambda eid=entry_id: self.show_view_entry(eid), cursor="hand2")
            view_btn.pack(side=tk.LEFT, padx=(0, 10))
            
            edit_btn = tk.Button(buttons_frame, text="Edit", font=('Inter', 10),
                                bg="#059669", fg="white", padx=15, pady=5,
                                command=lambda eid=entry_id: self.show_edit_entry(eid), cursor="hand2")
            edit_btn.pack(side=tk.LEFT, padx=(0, 10))
            
            delete_btn = tk.Button(buttons_frame, text="Delete", font=('Inter', 10),
                                  bg="#dc2626", fg="white", padx=15, pady=5,
                                  command=lambda eid=entry_id: self.delete_entry(eid), cursor="hand2")
            delete_btn.pack(side=tk.LEFT)
            
            # Character count
            char_count = len(content)
            count_label = tk.Label(buttons_frame, text=f"{char_count} characters", 
                                  font=('Inter', 9), fg="#9ca3af", bg="#ffffff")
            count_label.pack(side=tk.RIGHT)
    
    def show_create_entry(self):
        """Show create entry window"""
        self.show_entry_form("Create New Entry", "", "")
    
    def show_edit_entry(self, entry_id):
        """Show edit entry window"""
        entry = self.db.get_entry_by_id(entry_id)
        if entry:
            self.show_entry_form("Edit Entry", entry[1], entry[2], entry_id)
    
    def show_entry_form(self, window_title, title="", content="", entry_id=None):
        """Show entry form window (create or edit)"""
        form_window = tk.Toplevel(self.root)
        form_window.title(window_title)
        form_window.geometry("900x700")
        form_window.configure(bg="#f8fafc")
        form_window.transient(self.root)
        form_window.grab_set()
        
        # Main container
        main_frame = tk.Frame(form_window, bg="#f8fafc")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, text=window_title, font=('Inter', 20, 'bold'), 
                              fg="#1f2937", bg="#f8fafc")
        title_label.pack(pady=(0, 20))
        
        # Form frame
        form_frame = tk.Frame(main_frame, bg="#ffffff", relief="solid", borderwidth=1)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        form_content = tk.Frame(form_frame, bg="#ffffff")
        form_content.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Title field
        title_label = tk.Label(form_content, text="Title:", font=('Inter', 12, 'bold'), 
                              fg="#374151", bg="#ffffff")
        title_label.pack(anchor=tk.W, pady=(0, 5))
        
        title_entry = tk.Entry(form_content, font=('Inter', 14), width=80)
        title_entry.pack(fill=tk.X, pady=(0, 20))
        title_entry.insert(0, title)
        
        # Content field
        content_label = tk.Label(form_content, text="Content:", font=('Inter', 12, 'bold'), 
                                 fg="#374151", bg="#ffffff")
        content_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Text widget with scrollbar
        text_frame = tk.Frame(form_content, bg="#ffffff")
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        content_text = tk.Text(text_frame, font=('Inter', 12), wrap=tk.WORD, 
                              relief="solid", borderwidth=1)
        content_scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=content_text.yview)
        content_text.configure(yscrollcommand=content_scrollbar.set)
        
        content_text.pack(side="left", fill="both", expand=True)
        content_scrollbar.pack(side="right", fill="y")
        
        content_text.insert(1.0, self.clean_content_preview(content) if content else "")
        
        # Buttons frame
        buttons_frame = tk.Frame(form_content, bg="#ffffff")
        buttons_frame.pack(fill=tk.X, pady=(10, 0))
        
        cancel_btn = tk.Button(buttons_frame, text="Cancel", font=('Inter', 11),
                              bg="#6b7280", fg="white", padx=20, pady=8,
                              command=form_window.destroy, cursor="hand2")
        cancel_btn.pack(side=tk.LEFT)
        
        save_btn = tk.Button(buttons_frame, text="Save Entry", font=('Inter', 11, 'bold'),
                            bg="#4f46e5", fg="white", padx=20, pady=8,
                            command=lambda: self.save_entry(form_window, title_entry, content_text, entry_id), 
                            cursor="hand2")
        save_btn.pack(side=tk.RIGHT)
        
        title_entry.focus()
    
    def save_entry(self, window, title_entry, content_text, entry_id=None):
        """Save entry (create or update)"""
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
            self.update_entries_list()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save entry: {str(e)}")
    
    def show_view_entry(self, entry_id):
        """Show view entry window"""
        entry = self.db.get_entry_by_id(entry_id)
        if not entry:
            messagebox.showerror("Error", "Entry not found!")
            return
        
        entry_id, title, content, created_at, updated_at = entry
        
        view_window = tk.Toplevel(self.root)
        view_window.title(f"View: {title}")
        view_window.geometry("900x700")
        view_window.configure(bg="#f8fafc")
        view_window.transient(self.root)
        view_window.grab_set()
        
        # Main container
        main_frame = tk.Frame(view_window, bg="#f8fafc")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header frame
        header_frame = tk.Frame(main_frame, bg="#4f46e5")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        header_content = tk.Frame(header_frame, bg="#4f46e5")
        header_content.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        title_label = tk.Label(header_content, text=title, font=('Inter', 24, 'bold'), 
                              fg="white", bg="#4f46e5")
        title_label.pack(anchor=tk.W)
        
        created_date = datetime.fromisoformat(created_at.replace('Z', '+00:00')).strftime('%B %d, %Y at %I:%M %p')
        date_label = tk.Label(header_content, text=f"Created: {created_date}", 
                             font=('Inter', 12), fg="#c7d2fe", bg="#4f46e5")
        date_label.pack(anchor=tk.W, pady=(5, 0))
        
        if updated_at != created_at:
            updated_date = datetime.fromisoformat(updated_at.replace('Z', '+00:00')).strftime('%B %d, %Y at %I:%M %p')
            updated_label = tk.Label(header_content, text=f"Updated: {updated_date}", 
                                    font=('Inter', 12), fg="#c7d2fe", bg="#4f46e5")
            updated_label.pack(anchor=tk.W)
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg="#ffffff", relief="solid", borderwidth=1)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        content_container = tk.Frame(content_frame, bg="#ffffff")
        content_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Content text with scrollbar
        text_frame = tk.Frame(content_container, bg="#ffffff")
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        content_display = tk.Text(text_frame, font=('Inter', 12), wrap=tk.WORD, 
                                 relief="flat", borderwidth=0, state=tk.DISABLED)
        content_scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=content_display.yview)
        content_display.configure(yscrollcommand=content_scrollbar.set)
        
        # Insert and display content
        content_display.config(state=tk.NORMAL)
        content_display.insert(1.0, self.clean_content_preview(content))
        content_display.config(state=tk.DISABLED)
        
        content_display.pack(side="left", fill="both", expand=True)
        content_scrollbar.pack(side="right", fill="y")
        
        # Buttons frame
        buttons_frame = tk.Frame(content_container, bg="#ffffff")
        buttons_frame.pack(fill=tk.X)
        
        back_btn = tk.Button(buttons_frame, text="← Back to Dashboard", font=('Inter', 11),
                            bg="#6b7280", fg="white", padx=20, pady=8,
                            command=view_window.destroy, cursor="hand2")
        back_btn.pack(side=tk.LEFT)
        
        edit_btn = tk.Button(buttons_frame, text="Edit", font=('Inter', 11, 'bold'),
                            bg="#059669", fg="white", padx=20, pady=8,
                            command=lambda: [view_window.destroy(), self.show_edit_entry(entry_id)], 
                            cursor="hand2")
        edit_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        delete_btn = tk.Button(buttons_frame, text="Delete", font=('Inter', 11, 'bold'),
                              bg="#dc2626", fg="white", padx=20, pady=8,
                              command=lambda: [view_window.destroy(), self.delete_entry(entry_id)], 
                              cursor="hand2")
        delete_btn.pack(side=tk.RIGHT)
    
    def delete_entry(self, entry_id):
        """Delete an entry with confirmation"""
        result = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this entry?")
        if result:
            try:
                self.db.delete_entry(entry_id)
                messagebox.showinfo("Success", "Entry deleted successfully!")
                self.update_entries_list()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete entry: {str(e)}")
    
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
