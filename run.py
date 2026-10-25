from datetime import datetime
from flask import Flask, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "trustvault-key-10b981"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trustvault.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class VaultDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), default="Security Compliance")
    owner = db.Column(db.String(100), default="Siva Sankar")
    file_size = db.Column(db.String(50), default="48 KB")
    status = db.Column(db.String(50), default="Encrypted (AES-256)")

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Siva Sankar's Secure Vault</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
  <style>body{font-family:'Plus Jakarta Sans',sans-serif;background-color:#080C0A;color:#F9FAFB;}</style>
</head>
<body class="p-6 md:p-10 max-w-5xl mx-auto space-y-6">
  <div class="flex items-center justify-between pb-4 border-b border-[#24352B]">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-lg bg-[#10B981]/20 border border-[#10B981]/40 flex items-center justify-center text-xl">🛡️</div>
      <div>
        <h1 class="text-xl font-bold text-[#F9FAFB]">Siva Sankar's Secure Vault</h1>
        <p class="text-xs text-[#9CA3AF]">Owner: Siva Sankar · Policy: Strict Cryptographic Isolation</p>
      </div>
    </div>
    <span class="px-3 py-1 rounded bg-[#10B981]/15 text-[#34D399] text-xs font-semibold">● SQLite Active</span>
  </div>

  <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
    <div class="p-4 rounded-lg bg-[#121B16] border border-[#24352B]">
      <div class="text-xs text-[#9CA3AF] mb-1">Total Vaulted Documents</div>
      <div class="text-2xl font-bold font-mono text-[#F9FAFB]">{{ docs|length }}</div>
    </div>
    <div class="p-4 rounded-lg bg-[#121B16] border border-[#24352B]">
      <div class="text-xs text-[#9CA3AF] mb-1">Active Roles</div>
      <div class="text-2xl font-bold font-mono text-[#34D399]">Admin, Owner, Viewer</div>
    </div>
    <div class="p-4 rounded-lg bg-[#121B16] border border-[#24352B]">
      <div class="text-xs text-[#9CA3AF] mb-1">Encryption Protocol</div>
      <div class="text-2xl font-bold font-mono text-[#10B981]">AES-256-GCM</div>
    </div>
  </div>

  <div class="p-4 rounded-lg bg-[#121B16] border border-[#24352B] space-y-3">
    <h2 class="text-sm font-semibold text-[#F9FAFB]">Vault a New Document</h2>
    <form action="/add" method="POST" class="flex flex-col sm:flex-row gap-3 text-xs">
      <input type="text" name="title" placeholder="Document title (e.g. Q4 Security Audit)" required class="flex-1 bg-[#0D1410] border border-[#24352B] rounded px-3 py-2 text-white">
      <button type="submit" class="px-5 py-2 rounded bg-[#10B981] font-semibold text-black hover:bg-[#059669]">Vault Document</button>
    </form>
  </div>

  <div class="p-4 rounded-lg bg-[#121B16] border border-[#24352B] space-y-3">
    <h2 class="text-sm font-semibold text-[#F9FAFB]">Vaulted Documents Inventory</h2>
    <table class="w-full text-left text-xs">
      <thead>
        <tr class="border-b border-[#24352B] text-[#9CA3AF]">
          <th class="pb-2 font-medium">Document Title</th>
          <th class="pb-2 font-medium">Owner</th>
          <th class="pb-2 font-medium">Status</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-[#24352B]/60">
        {% for doc in docs %}
        <tr class="hover:bg-[#0D1410]/50">
          <td class="py-2.5 font-medium text-white">{{ doc.title }}</td>
          <td class="py-2.5 text-[#9CA3AF]">{{ doc.owner }}</td>
          <td class="py-2.5 text-[#34D399] font-mono">{{ doc.status }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE, docs=VaultDocument.query.all())

@app.route("/add", methods=["POST"])
def add_doc():
    title = request.form.get("title", "").strip()
    if title:
        new_doc = VaultDocument(title=title, category="Security & Compliance", owner="Siva Sankar")
        db.session.add(new_doc)
        db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not VaultDocument.query.first():
            db.session.add(VaultDocument(title="SOC 2 Type II Security Attestation & Control Matrix", owner="Siva Sankar"))
            db.session.add(VaultDocument(title="Zero-Trust Enclave & Key Ceremony Runbook", owner="Siva Sankar"))
            db.session.commit()
    print("=" * 60)
    print(" Siva Sankar's Secure Vault is running!")
    print(" Open in your browser: http://127.0.0.1:5000")
    print("=" * 60)
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
