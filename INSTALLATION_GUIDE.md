# HEAVE v1.0.0 — Installation Guide

**Version:** 1.0.0  
**Last Updated:** July 6, 2026  
**Status:** Production Release

---

## System Requirements

### Minimum Requirements
- **OS:** Windows 10 (Build 19041) or later
- **RAM:** 4 GB
- **Storage:** 500 MB free disk space
- **Display:** 1024 × 768 minimum resolution
- **Network:** Internet connection for cloud AI features

### Recommended Requirements
- **OS:** Windows 11 Pro/Enterprise
- **RAM:** 8 GB or more
- **Storage:** 1 GB SSD
- **Display:** 1920 × 1080 or higher
- **Network:** Broadband (25+ Mbps)

### Supported Operating Systems
- ✅ Windows 11 (recommended)
- ✅ Windows 10 (supported)
- ⏳ macOS (in development)
- ⏳ Linux (in development)

---

## Installation Methods

### Method 1: Windows Installer (Recommended)

#### Step 1: Download the Installer
1. Visit the HEAVE release page
2. Download `HEAVE-v1.0.0-Setup.exe`
3. Verify file size is approximately 150-200 MB

#### Step 2: Run the Installer
1. Double-click `HEAVE-v1.0.0-Setup.exe`
2. Click "Next" on the welcome screen
3. Review the license agreement and click "I Agree"
4. Choose installation directory (default: `C:\Program Files\HEAVE`)
5. Click "Install"
6. Wait for installation to complete (2-3 minutes)
7. Click "Finish"

#### Step 3: Launch HEAVE
- The installer will automatically launch HEAVE
- Or find HEAVE in Start Menu and click to launch

#### Step 4: Initial Configuration
1. The backend will initialize automatically
2. Default database will be created
3. You'll see the login screen
4. Default credentials: `vrushh_98` / `Vrush@nk09`

---

### Method 2: Portable Version

#### Step 1: Download the Portable Package
1. Download `HEAVE-v1.0.0-portable.zip`
2. Extract to desired location (e.g., `C:\HEAVE`)

#### Step 2: Run HEAVE
1. Navigate to extracted folder
2. Double-click `HEAVE.exe`
3. Backend will initialize automatically

#### Pros:
- No installation required
- Can run from USB drive
- No registry modifications

#### Cons:
- Must run from the same location
- Updates are manual

---

### Method 3: Development Installation

For developers who want to build from source:

#### Prerequisites
- Node.js 18+ ([Download](https://nodejs.org))
- Python 3.9+ ([Download](https://www.python.org))
- Git ([Download](https://git-scm.com))
- Rust (for Tauri) ([Install](https://rustup.rs))

#### Step 1: Clone Repository
```bash
git clone https://github.com/vrushh/heave.git
cd heave
```

#### Step 2: Install Dependencies
```bash
# Install Node dependencies
npm install

# Install Python dependencies
cd backend
pip install -r requirements.txt
cd ..
```

#### Step 3: Start Development Server
```bash
# Terminal 1: Start backend
cd backend
python -m main

# Terminal 2: Start frontend (new terminal)
npm run dev
```

The app will open at `http://localhost:5173`

#### Step 4: Build for Production
```bash
npm run build
# Output: src-tauri/target/release/HEAVE.exe
```

---

## First Launch & Setup

### Initial Login
1. **Username:** `vrushh_98`
2. **Password:** `Vrush@nk09`
3. Click "Login"

### Post-Login Setup
1. **Change Password:** Settings > Security > Change Password
2. **Set AI Provider:** Settings > AI Providers > Add Provider
3. **Configure Workspace:** Settings > Workspaces > Select Default
4. **Customize Theme:** Settings > Appearance > Theme

---

## Configuration

### Backend Configuration (Advanced)

Edit `backend/.env`:

```env
# Development mode (disable for production)
DEBUG=False

# Logging level: DEBUG, INFO, WARNING, ERROR
LOG_LEVEL=INFO

# Database configuration
DATABASE_URL=sqlite:///./heave.db

# API settings
API_HOST=127.0.0.1
API_PORT=8000

# Security
SECRET_KEY=your-unique-secret-key-here  # CHANGE IN PRODUCTION
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS (for development)
CORS_ORIGINS=["tauri://localhost", "http://localhost:5173"]
```

### Important Security Notes

⚠️ **For Production:**
1. Change `SECRET_KEY` to a random, strong value:
   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(32))"
   ```

2. Set `DEBUG=False`

3. Change `API_PORT` to a non-standard port

4. Configure CORS properly if using reverse proxy

---

## AI Provider Setup

### OpenAI
1. Get API key from [openai.com/api](https://openai.com/api)
2. In HEAVE: Settings > AI Providers > Add Provider
3. Select "OpenAI"
4. Paste API key
5. Click "Test Provider" to verify

### Anthropic (Claude)
1. Get API key from [console.anthropic.com](https://console.anthropic.com)
2. In HEAVE: Settings > AI Providers > Add Provider
3. Select "Anthropic"
4. Paste API key
5. Click "Test Provider"

### Local Models (Ollama/LM Studio)
1. Install Ollama: [ollama.ai](https://ollama.ai)
2. Start Ollama and pull a model: `ollama pull mistral`
3. In HEAVE: Settings > AI Providers > Add Provider
4. Select "Ollama"
5. Verify local connection: `http://localhost:11434`
6. Click "Test Provider"

### Other Providers
- **Google Gemini:** [ai.google.dev](https://ai.google.dev)
- **OpenRouter:** [openrouter.ai](https://openrouter.ai)
- **Hugging Face:** [huggingface.co](https://huggingface.co)

---

## Security Setup

### 1. Change Default Password
```
Settings > Security > Change Password
Old: heave
New: (your strong password)
```

### 2. Enable Security Level
```
Settings > Security > Security Level
- Basic: Casual use
- Standard: Regular protection (recommended)
- Advanced: High security
- Maximum: Maximum security + all features
```

### 3. Set PIN Unlock (Optional)
```
Settings > Security > PIN
Enable PIN
Enter 4-digit PIN
```

### 4. Enable Biometric (Windows Hello)
```
Settings > Security > Biometric
Select Face or Fingerprint
Enroll with Windows Hello
```

### 5. Encrypted Backup
```
Settings > Backup > Enable Encryption
Create encrypted backup
Store backup securely
```

---

## Troubleshooting

### HEAVE Won't Start

**Error: "Backend connection failed"**
- Backend is not running
- Solution: Ensure backend port 8000 is available
- Try: `netstat -ano | findstr :8000`

**Error: "Database locked"**
- Another instance of HEAVE is running
- Solution: Close all HEAVE windows and restart

### Login Issues

**Error: "Invalid credentials"**
- Username or password incorrect
- Check caps lock
- Reset with: `Settings > Reset Password` (if available)

**Error: "Connection timeout"**
- Backend is not reachable
- Check firewall settings
- Verify backend is running: `curl http://localhost:8000`

### Performance Issues

**HEAVE is slow**
- Disable animations: Settings > Accessibility > Reduce Motion
- Clear cache: Settings > Maintenance > Clear Cache
- Restart HEAVE: Close and reopen

**High memory usage**
- Close unused workspaces
- Archive old notes and projects
- Clear downloads/uploads folder

### Database Issues

**Error: "Database corrupted"**
- Restore from backup
- Delete `.db` file and restart (WARNING: data loss)
- Check backup in: Settings > Backup & Restore

**Error: "Disk full"**
- Delete old notes/files
- Run maintenance: Settings > Maintenance > Run Now
- Check disk space: `Get-Volume` (PowerShell)

---

## Uninstallation

### Uninstall HEAVE

#### Windows Installer
1. Go to Settings > Apps > Apps & features
2. Find "HEAVE" in the list
3. Click "Uninstall"
4. Confirm deletion

#### Data Removal
By default, your data is saved in:
```
C:\Users\[YourUsername]\AppData\Roaming\HEAVE
```

To completely remove data:
1. Delete the HEAVE folder above
2. Or export data first via Settings > Export

### Reinstall
1. Download latest installer
2. Run installation
3. Data will persist if AppData folder wasn't deleted

---

## Backup & Recovery

### Create Backup
1. Settings > Backup & Restore > Create Backup
2. Choose location to save
3. Optionally encrypt backup
4. Backup completes (~1 minute)

### Restore from Backup
1. Settings > Backup & Restore > Restore
2. Select backup file
3. Confirm restoration
4. HEAVE restarts with restored data

### Backup Location
Default: `C:\Users\[YourUsername]\Documents\HEAVE_Backups`

---

## Updating HEAVE

### Check for Updates
```
Settings > About > Check for Updates
```

### Install Update
1. Click "Update Available" notification
2. Click "Download & Install"
3. Wait for download (usually < 5 minutes)
4. Click "Install"
5. HEAVE restarts with new version

### Manual Update
1. Download new installer
2. Run installer (will upgrade existing version)
3. Select "Upgrade" when prompted

---

## Getting Help

### In-App Help
- Settings > Help > User Guide
- Settings > Help > Keyboard Shortcuts
- Settings > Help > About HEAVE

### Documentation
- User Guide: [docs/USER_GUIDE.md](docs/USER_GUIDE.md)
- FAQ: [docs/FAQ.md](docs/FAQ.md)
- Troubleshooting: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

### Support
- **Email:** support@heave.com
- **GitHub Issues:** [github.com/vrushh/heave/issues](https://github.com/vrushh/heave/issues)

---

## What's Next?

After installation:

1. **Add AI Provider** (OpenAI, Anthropic, or Local)
2. **Explore Settings** and customize preferences
3. **Create First Note** to test basic functionality
4. **Enable Security** (PIN or biometric)
5. **Create Backup** for data protection
6. **Read User Guide** for advanced features

---

## Advanced Installation

### Server Deployment (FastAPI)

Deploy backend to a server:

```bash
# Install dependencies
pip install -r backend/requirements.txt

# Run with Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

# Or with gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

### Docker Installation

```dockerfile
FROM python:3.9
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Reverse Proxy (Nginx)

```nginx
server {
    listen 443 ssl;
    server_name heave.example.com;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## FAQ

**Q: Is HEAVE free?**  
A: HEAVE v1.0.0 is available for personal use. Commercial licensing information is available at [heave.com/licensing](https://heave.com/licensing).

**Q: Can I run HEAVE on macOS or Linux?**  
A: macOS and Linux support are in development for v2.0.

**Q: How do I backup my data?**  
A: Use Settings > Backup & Restore > Create Backup. Store backups securely.

**Q: Can I move HEAVE to another computer?**  
A: Yes. Backup on source, uninstall, install on new computer, restore backup.

**Q: Is my data encrypted?**  
A: Data is encrypted at rest optionally. API keys and passwords are always encrypted.

---

## Version Information

- **Current Version:** 1.0.0
- **Release Date:** July 6, 2026
- **Update Channel:** Stable
- **Next Release:** v1.1.0 (scheduled)

---

## Legal

- **License:** Commercial (See LICENSE.md)
- **Privacy:** HEAVE processes all data locally; no analytics sent
- **Terms of Service:** [heave.com/tos](https://heave.com/tos)

---

**HEAVE v1.0.0 is ready to use. Welcome!**

For questions or issues, contact support or open an issue on GitHub.
