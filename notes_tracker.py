

print("📚 SCHOOL NOTES TRACKER")
print("Organize and track your school notes efficiently!")

# Global variables to store subjects and notes
subjects = []      # List to store all subjects
notes = []         # List to store all notes
subject_counter = 1  # Counter to generate unique subject IDs
note_counter = 1     # Counter to generate unique note IDs

def main_menu():
    # Main menu function that runs the entire application
    while True:
        # Display menu options
        print("\n" + "="*40)
        print("           MAIN MENU")
        print("="*40)
        print("1. Add Subject")
        print("2. Add Note") 
        print("3. View All Subjects")
        print("4. View Notes by Subject")
        print("5. Search Notes")
        print("6. Exit")
        print("="*40)
        
        # Get user choice
        choice = input("Enter your choice (1-6): ")
        
        # Process user choice
        if choice == "1":
            add_subject()
        elif choice == "2":
            add_note()
        elif choice == "3":
            view_all_subjects()
        elif choice == "4":
            view_notes_by_subject()
        elif choice == "5":
            search_notes()
        elif choice == "6":
            print("👋 Thank you for using School Notes Tracker!")
            break
        else:
            print("Invalid choice! Please enter 1-6.")

def add_subject():
    # Function to add a new subject
    global subject_counter  # Use global counter
    
    print("\n--- Add New Subject ---")
    subject_name = input("Subject name: ")
    
    # Create new subject dictionary
    new_subject = {
        'id': subject_counter,      # Unique ID for subject
        'name': subject_name,       # Subject name
        'note_count': 0             # Count of notes in this subject
    }
    
    # Add subject to list and increment counter
    subjects.append(new_subject)
    subject_counter += 1
    print(f"Subject '{subject_name}' added successfully!")

def add_note():
    # Function to add a new note to a subject
    global note_counter  # Use global counter
    
    # Check if subjects exist
    if not subjects:
        print("Please add a subject first!")
        return
    
    print("\n--- Add New Note ---")
    view_all_subjects()  # Show available subjects
    
    subject_id_input = input("Enter subject ID: ")
    
    # Validate subject ID input
    if subject_id_input.isdigit():
        subject_id = int(subject_id_input)
        
        # Find the subject by ID
        subject_found = None
        for subject in subjects:
            if subject['id'] == subject_id:
                subject_found = subject
                break
        
        # If subject found, get note details
        if subject_found:
            note_title = input("Note title: ")
            note_content = input("Note content: ")
            priority = input("Priority (High/Medium/Low): ")
            
            # Create new note dictionary
            new_note = {
                'id': note_counter,              # Unique ID for note
                'subject_id': subject_id,        # ID of the subject
                'subject_name': subject_found['name'],  # Name of the subject
                'title': note_title,             # Note title
                'content': note_content,         # Note content
                'priority': priority,            # Priority level
                'completed': False               # Completion status
            }
            
            # Add note to list and update counters
            notes.append(new_note)
            subject_found['note_count'] += 1  # Increase note count for subject
            note_counter += 1
            print(f"Note '{note_title}' added successfully!")
        else:
            print("Subject not found!")
    else:
        print("Please enter a valid subject ID!")

def view_all_subjects():
    # Function to display all subjects
    if not subjects:
        print("No subjects added yet!")
        return
    
    # Display subjects in formatted table
    print("\n" + "="*50)
    print(f"{'ALL SUBJECTS':^50}")
    print("="*50)
    print(f"{'ID':<5} {'Subject Name':<20} {'Note Count':<15}")
    print("-"*50)
    
    # Print each subject
    for subject in subjects:
        print(f"{subject['id']:<5} {subject['name']:<20} {subject['note_count']:<15}")
    
    print("="*50)

def view_notes_by_subject():
    # Function to view notes for a specific subject
    if not subjects:
        print("No subjects added yet!")
        return
    
    view_all_subjects()  # Show available subjects
    subject_id_input = input("Enter subject ID to view notes: ")
    
    # Validate subject ID input
    if subject_id_input.isdigit():
        subject_id = int(subject_id_input)
        
        # Collect all notes for this subject
        subject_notes = []
        for note in notes:
            if note['subject_id'] == subject_id:
                subject_notes.append(note)
        
        # Display notes if found
        if subject_notes:
            subject_name = subject_notes[0]['subject_name']
            print(f"\n📖 Notes for {subject_name}:")
            print("="*60)
            print(f"{'ID':<5} {'Title':<20} {'Priority':<10} {'Status':<10}")
            print("-"*60)
            
            # Print each note in the subject
            for note in subject_notes:
                status = "Done" if note['completed'] else "Pending"
                print(f"{note['id']:<5} {note['title']:<20} {note['priority']:<10} {status:<10}")
            
            print("="*60)
            
            # Option to view note details
            note_id_input = input("Enter note ID to view details (or press Enter to skip): ")
            if note_id_input.isdigit():
                note_id = int(note_id_input)
                # Find and display note details
                for note in subject_notes:
                    if note['id'] == note_id:
                        print(f"\n📝 Note Details:")
                        print(f"Title: {note['title']}")
                        print(f"Subject: {note['subject_name']}")
                        print(f"Priority: {note['priority']}")
                        print(f"Status: {'Completed' if note['completed'] else 'Not Completed'}")
                        print(f"Content: {note['content']}")
                        break
        else:
            print("No notes found for this subject!")
    else:
        print("Please enter a valid subject ID!")

def search_notes():
    # Function to search notes by title or content
    if not notes:
        print("No notes added yet!")
        return
    
    print("\n--- Search Notes ---")
    search_term = input("Enter search term (title or content): ").lower()
    
    # Search for notes containing the search term
    found_notes = []
    for note in notes:
        if search_term in note['title'].lower() or search_term in note['content'].lower():
            found_notes.append(note)
    
    # Display search results
    if found_notes:
        print(f"\n🔍 Found {len(found_notes)} note(s):")
        print("="*60)
        print(f"{'ID':<5} {'Title':<20} {'Subject':<15} {'Priority':<10}")
        print("-"*60)
        
        # Print each found note
        for note in found_notes:
            print(f"{note['id']:<5} {note['title']:<20} {note['subject_name']:<15} {note['priority']:<10}")
        
        print("="*60)
    else:
        print("No notes found matching your search!")

# Start the program
main_menu()