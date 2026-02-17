# Google Sheets Persistence Setup

Enables crisis reports, aid registrations, and accountability submissions
to persist across sessions — stored in your own Google Sheet.

**Time required:** ~8 minutes  
**Cost:** Free (Google Apps Script)  
**Data ownership:** Entirely yours — sits in your Google Drive

---

## Step 1 — Create the Sheet

1. Go to [sheets.google.com](https://sheets.google.com)
2. Create a new spreadsheet → name it **GospelMap Submissions**
3. Note the spreadsheet URL (you don't need the ID explicitly)

---

## Step 2 — Add the Apps Script

1. In the spreadsheet: **Extensions → Apps Script**
2. Delete the default code, paste this:

```javascript
function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    
    // Get or create a sheet tab for each form_type
    var sheetName = data.form_type || "submissions";
    var sheet = ss.getSheetByName(sheetName);
    if (!sheet) {
      sheet = ss.insertSheet(sheetName);
    }
    
    // Write header row if sheet is empty
    if (sheet.getLastRow() === 0) {
      var headers = Object.keys(data);
      sheet.appendRow(headers);
    }
    
    // Append data row
    var values = Object.values(data);
    sheet.appendRow(values);
    
    return ContentService
      .createTextOutput(JSON.stringify({status: "ok"}))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch(err) {
    return ContentService
      .createTextOutput(JSON.stringify({status: "error", message: err.toString()}))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Test function — run this once to verify it works
function testPost() {
  var test = {
    "form_type": "test",
    "message": "GospelMap connection working",
    "timestamp": new Date().toISOString()
  };
  var e = {postData: {contents: JSON.stringify(test)}};
  Logger.log(doPost(e).getContent());
}
```

3. Click **Save** (floppy disk icon)

---

## Step 3 — Deploy as Web App

1. Click **Deploy → New Deployment**
2. Click the gear icon ⚙️ next to "Select type" → choose **Web app**
3. Set:
   - **Execute as:** Me (your Google account)
   - **Who has access:** Anyone
4. Click **Deploy**
5. **Copy the Web App URL** — it looks like:
   `https://script.google.com/macros/s/AKfyc.../exec`

---

## Step 4 — Add to Streamlit Cloud Secrets

1. Go to your [Streamlit Cloud dashboard](https://share.streamlit.io)
2. Find your GospelMap app → **⋮ → Settings → Secrets**
3. Add:

```toml
SHEETS_ENDPOINT = "https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec"
```

4. **Save** — the app will reload automatically

---

## What Gets Stored

Each form submission creates a row in a separate sheet tab:

| Tab Name | Created By |
|----------|-----------|
| `crisis_report` | Crisis Response → Report a New Crisis |
| `aid_capacity` | Crisis Response → Offer Aid Capacity |
| `accountability_submission` | Accountability → Submit Data |
| `justice_campaign` | Justice Network → Submit a Campaign |

---

## Verification

After setup, submit a test crisis report. Within seconds you should see
a new row in the **crisis_report** tab of your Google Sheet.

The banner in the app changes from:
> "Session only — connect Google Sheets to persist"

to:
> "Saved to network registry."

---

## Privacy Notes

- All submissions go directly to **your** Google Drive
- No data passes through any third-party server
- Users are not tracked individually
- Sensitive submissions (abuse records) should be submitted via email
  to contact@aikungfu.dev instead of this form

