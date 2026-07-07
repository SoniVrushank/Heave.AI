# HEAVE v1.0.0 — User Guide

**Version:** 1.0.0  
**Last Updated:** July 6, 2026

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Core Features](#core-features)
3. [Workspaces & Companies](#workspaces--companies)
4. [Notes & Content](#notes--content)
5. [Tasks & Projects](#tasks--projects)
6. [AI Features](#ai-features)
7. [Plugins & Integrations](#plugins--integrations)
8. [Settings & Customization](#settings--customization)
9. [Security & Privacy](#security--privacy)
10. [Tips & Tricks](#tips--tricks)

---

## Getting Started

### Login
1. Launch HEAVE
2. Enter username: `vrushh_01`
3. Enter password: `heave` (default)
4. Click "Login"

### First Time Setup
1. Change your password immediately
2. Set a default workspace
3. Add at least one AI provider
4. Configure security settings

### Dashboard Overview
- **Left Sidebar:** Navigation (Notes, Tasks, Projects, etc.)
- **Main Panel:** Content editor/viewer
- **Right Panel:** Details and metadata
- **Top Bar:** Search, notifications, settings

---

## Core Features

### Notes
Create and organize rich text notes with formatting.

**Create a Note:**
1. Click "Notes" in sidebar
2. Click "New Note"
3. Enter title and content
4. Click "Save" (Ctrl+S)

**Format Text:**
- **Bold:** Ctrl+B or select text > **Bold**
- *Italic:* Ctrl+I
- Underline: Ctrl+U
- Links: Ctrl+K
- Code: Backticks ` `

**Organize Notes:**
- Add tags: Click "Add Tags" at bottom
- Set workspace: Top of editor
- Pin important: Click pin icon
- Archive old: Right-click > Archive

### Tasks
Create actionable tasks with priorities and deadlines.

**Create a Task:**
1. Click "Tasks" in sidebar
2. Click "New Task"
3. Enter title and description
4. Set priority (Low/Medium/High/Urgent)
5. Set due date (optional)
6. Click "Save"

**Track Progress:**
- Mark complete: Click checkbox
- Update status: (Open/In Progress/Done)
- Add subtasks: Click "+" in task details
- Set reminders: Click bell icon

### Projects
Organize related tasks and files into projects.

**Create a Project:**
1. Click "Projects" in sidebar
2. Click "New Project"
3. Enter name and description
4. Set status (Planning/Active/On Hold/Complete)
5. Click "Create"

**Manage Project:**
- Add tasks: Click "Add Task"
- Upload files: Click "Upload"
- Track progress: View completion bar
- Archive when done: Project menu > Archive

### Files
Store and organize documents and media.

**Upload File:**
1. Click "Files" in sidebar
2. Click "Upload"
3. Select file from computer
4. Click "Open"
5. File appears in list

**Manage Files:**
- Organize in folders
- Download: Click file > Download
- Share: Generate public link (coming v2.0)
- Delete: Right-click > Delete

### Calendar
Schedule events and view your timeline.

**Create Event:**
1. Click "Calendar" in sidebar
2. Click on date/time
3. Enter event details
4. Set reminder
5. Click "Save"

**View Calendar:**
- Month view: Default
- Week view: Click "Week"
- Agenda view: Click "Agenda"
- Add to external: Google Calendar sync (v2.0)

---

## Workspaces & Companies

### What's a Workspace?
Workspaces are organizational containers. Each workspace can have its own:
- Notes, tasks, projects
- Files and documents
- Settings and preferences
- Team members (future)

**Default Workspaces:**
- Personal: Your private space
- Hevify: Client work
- VPAG: Business operations
- Clients: Future clients

### Switch Workspace
1. Click workspace name in sidebar
2. Select different workspace from dropdown
3. Content updates to show that workspace

### Create Custom Workspace
1. Settings > Workspaces > New Workspace
2. Enter name and icon
3. Set color
4. Click "Create"

### What's a Company?
Companies provide workspace isolation for enterprise use. Each company has:
- Separate data store
- Own user accounts
- Workspace hierarchy
- Data never mixed between companies

---

## Notes & Content

### Rich Text Formatting
- Headings: `# H1` `## H2` `### H3`
- Lists: `- ` or `* ` for bullets
- Numbered: `1. ` or `1) `
- Code blocks: Triple backticks
- Blockquotes: `> `
- Horizontal line: `---`

### Search Notes
1. Click search bar (top)
2. Type keywords
3. Results appear instantly
4. Click to open note

### Advanced Search
- Search by tag: `tag:important`
- Search by workspace: `workspace:personal`
- Search by date: `date:2024-07`
- Combine: `tag:work workspace:projects`

### Export Notes
1. Right-click note
2. Click "Export"
3. Choose format (Markdown/PDF/Word)
4. Save to computer

---

## Tasks & Projects

### Task Statuses
- **Open:** New task, not started
- **In Progress:** Currently working on it
- **Done:** Completed task

### Task Priorities
- **Low:** Can wait, nice to have
- **Medium:** Important, needs doing
- **High:** Urgent, due soon
- **Urgent:** Critical, do now

### Due Dates
- Set deadline: Click calendar icon
- Recurring: Set "Repeat" option
- Overdue: Task turns red after deadline
- Reminders: Get notification before due

### Subtasks
Break large tasks into smaller ones:
1. Open task
2. Click "+ Add subtask"
3. Enter subtask title
4. Check off as completed

### Project Dashboard
1. Click "Projects"
2. View all projects with progress
3. Click project to open
4. See tasks, files, timeline
5. Track completion percentage

---

## AI Features

### What is Hirvi?
Hirvi is your personal AI assistant. Features:

**Chat:**
- Natural conversation
- Context awareness
- Multiple AI providers
- History saved locally

**Quick Actions:**
- Summarize: Select text > AI > Summarize
- Expand: Select text > AI > Expand
- Rewrite: Select text > AI > Rewrite
- Translate: Select text > AI > Translate

### Change AI Provider
1. Settings > AI Providers
2. Select default provider
3. Click "Set as Default"

**Available Providers:**
- OpenAI (ChatGPT)
- Anthropic (Claude)
- Google Gemini
- Local (Ollama, LM Studio)
- OpenRouter (aggregate)

### AI Provider Settings
1. Settings > AI Providers > Add Provider
2. Select provider type
3. Paste API key
4. Click "Test Connection"
5. If pass, provider is ready to use

**Getting API Keys:**
- OpenAI: [openai.com/api](https://openai.com/api)
- Anthropic: [console.anthropic.com](https://console.anthropic.com)
- Google: [ai.google.dev](https://ai.google.dev)

### Customize Hirvi
1. Settings > General > Hirvi Name
2. Enter new name (1-50 chars)
3. Changes apply everywhere
4. Click "Save"

---

## Plugins & Integrations

### What are Plugins?
Plugins extend HEAVE with external integrations:
- Google Drive, GitHub, Slack, Discord
- Notion, Figma, VS Code
- Gmail, Calendar, Docs, WhatsApp

### Install Plugin
1. Settings > Plugins > Available
2. Click plugin to install
3. Enter credentials/API key
4. Click "Install"
5. Plugin appears in sidebar

### Configure Plugin
1. Settings > Plugins > Installed
2. Click plugin > Settings
3. Update credentials or settings
4. Save changes

### Plugin Status
- **Connected:** Fully operational
- **Disconnected:** Credentials invalid
- **Error:** Check logs and reconnect
- **Updating:** Auto-installing latest version

### Remove Plugin
1. Settings > Plugins > Installed
2. Click plugin > Remove
3. Confirm removal
4. Data associated with plugin is archived

---

## Settings & Customization

### General Settings
**Theme:**
- Dark (default): Easy on eyes
- Light: Bright mode
- Auto: Follow system

**Language:**
- English (default)
- Spanish, French, German (v2.0)

**Appearance:**
- Reduce Motion: Disable animations
- Increase Contrast: High contrast mode
- Font Scale: 1.0× to 1.5×
- Disable Transparency: Solid colors

### Workspace Settings
**Preferences:**
- Set default workspace
- Auto-sync enabled
- Notifications on/off
- Auto-logout after X minutes

### Security Settings
**Password:**
1. Settings > Security > Change Password
2. Enter current password
3. Enter new password (strong)
4. Confirm new password
5. Click "Save"

**Security Level:**
1. Settings > Security > Security Level
2. Choose level:
   - Basic: Casual use
   - Standard: Regular protection (recommended)
   - Advanced: High security
   - Maximum: Maximum security
3. Settings auto-configure

**PIN Unlock:**
1. Settings > Security > PIN
2. Click "Enable PIN"
3. Enter 4-6 digit PIN
4. Confirm PIN
5. PIN required to unlock

**Biometric (Windows Hello):**
1. Settings > Security > Biometric
2. Click "Face" or "Fingerprint"
3. Follow Windows Hello enrollment
4. Biometric becomes unlock method

**Session Timeout:**
1. Settings > Security > Session Timeout
2. Set minutes before auto-logout
3. 0 = disabled
4. Useful for security level

---

## Security & Privacy

### Data Protection
- All data stored locally on your computer
- Passwords hashed with bcrypt
- API keys encrypted with Fernet
- No data sent to servers (except AI calls)

### Backup Data
1. Settings > Backup & Restore > Create Backup
2. Optional: Enable encryption
3. Choose backup location
4. Click "Create Backup"
5. Backup saves as `.heave` file

### Restore Data
1. Settings > Backup & Restore > Restore
2. Select `.heave` backup file
3. Confirm restoration
4. HEAVE restarts with data

### Privacy Controls
**Notification Privacy:**
- When enabled: Don't show preview text
- Useful in shared environments
- Toggle: Settings > Security > Notification Privacy

**Clipboard Protection:**
- When enabled: Don't copy sensitive data
- API keys protected in clipboard
- Toggle: Settings > Security > Clipboard Protection

### Data Deletion
**Soft Delete (Archive):**
- Archive notes: Right-click > Archive
- Data still recoverable
- Hidden from normal view

**Permanent Delete:**
- Delete note: Right-click > Delete
- Confirmation required
- Cannot be recovered (restore from backup)

**Full Reset:**
1. Settings > Advanced > Reset HEAVE
2. Careful: This deletes everything
3. Requires backup first
4. Restores factory settings

---

## Tips & Tricks

### Keyboard Shortcuts
- **Ctrl+N:** New note
- **Ctrl+T:** New task
- **Ctrl+S:** Save current item
- **Ctrl+F:** Search
- **Ctrl+,:** Settings
- **Ctrl+?:** Keyboard shortcuts
- **Ctrl+K:** Insert link

### Power Features

**Universal Search:**
- Search everything from one place
- Press `/` from any screen
- Instant results across all data
- Filter by type (notes, tasks, etc.)

**Quick Add:**
- Press `Ctrl+Alt+N` from anywhere
- Creates note in current workspace
- Type and continue working

**Tags:**
- Add tags to notes, tasks
- Search by tag: `tag:important`
- Create custom tag groups
- Organize without folders

**Templates:**
- Create template from note
- Reuse structure for new items
- Save time on recurring tasks

**Automations:**
- Set up automation rules
- Example: Auto-archive completed tasks
- Notification triggers
- Scheduled actions

### Memory System
HEAVE remembers important information:
- **Personal Memory:** Your preferences, style
- **Company Memory:** Business info, knowledge
- **General Memory:** Notes for Hirvi to use

To record memory:
1. Select text in note
2. Click AI > "Remember This"
3. Memory is saved for later

### Monthly Maintenance
Runs automatically on 14th of month:
- Database optimization
- Cache cleanup
- Temporary file removal
- Backup creation
- Skill auto-refresh

View report: Settings > Maintenance > Last Report

---

## Troubleshooting

### HEAVE is slow
**Solution:**
1. Disable animations: Settings > Accessibility > Reduce Motion
2. Close unused workspace tabs
3. Run maintenance: Settings > Maintenance > Run Now
4. Restart HEAVE

### Lost data
**Solution:**
1. Restore from backup: Settings > Backup & Restore > Restore
2. Select recent backup file
3. Confirm restoration
4. Check for recovered data

### AI not working
**Solution:**
1. Check AI provider: Settings > AI Providers
2. Test provider: Click "Test" button
3. Verify API key is correct
4. Check internet connection
5. Try different provider

### Backup/restore errors
**Solution:**
1. Ensure destination has space
2. Close other HEAVE windows
3. Check file permissions
4. Try manual backup first
5. Check logs: Settings > Logs

### Performance issues
**Solution:**
1. Archive old notes/tasks
2. Delete unused files
3. Clear browser cache
4. Restart HEAVE
5. Check RAM usage: Task Manager

---

## Advanced Topics

### Research System
Deep research capture for complex topics:
1. Click "Research"
2. Click "New Research"
3. Enter research question
4. Add sources (links, documents)
5. Add findings and notes
6. Organize with tags
7. Export as report

### Analytics
View your usage statistics:
1. Click "Analytics"
2. View activity by day/week/month
3. Most used features
4. Productivity trends
5. Time spent per category

### Integrations
Connect external services:
1. Click "Integrations"
2. Choose service (Slack, Discord, etc.)
3. Authorize connection
4. Configure options
5. Start using integration

---

## Frequently Asked Questions

**Q: Can I sync across devices?**  
A: v1.0 is local-only. v2.0 will have cloud sync.

**Q: How much data can I store?**  
A: Limited by your disk space (tested to 100GB+).

**Q: Can I collaborate with others?**  
A: Team features coming in v2.0.

**Q: Is HEAVE available offline?**  
A: Yes! Everything works offline except cloud AI.

**Q: How do I report a bug?**  
A: Settings > Help > Report Bug, or email support.

**Q: Can I export all my data?**  
A: Yes. Settings > Export > Choose format and scope.

---

## Getting Help

### Built-in Help
- **Settings > Help > User Guide** (this document)
- **Settings > Help > Keyboard Shortcuts**
- **Settings > Help > About HEAVE**

### External Resources
- **GitHub:** [github.com/vrushh/heave](https://github.com/vrushh/heave)
- **Email:** support@heave.com
- **Documentation:** See `docs/` folder in installation

---

## Next Steps

1. ✅ **Read this guide** (you're here!)
2. 📝 **Create your first note**
3. ✅ **Add a task**
4. 🤖 **Set up an AI provider**
5. 🔒 **Change your password**
6. 💾 **Create a backup**

---

**Welcome to HEAVE! Start building your personal AI operating system.**

For more information, visit the documentation or contact support.

---

**HEAVE v1.0.0 — Your Personal AI Begins Here**
