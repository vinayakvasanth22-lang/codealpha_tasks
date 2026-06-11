"""
TASK 3: Task Automation with Python Scripts
Covers all three ideas:
  1. Move all .jpg files from a folder to a new folder
  2. Extract all email addresses from a .txt file and save them
  3. Scrape the title of a fixed webpage and save it
Key concepts: os, shutil, re, requests, file handling
"""

import os
import shutil
import re

# ─────────────────────────────────────────────
# TASK 1 — Move all .jpg files to a new folder
# ─────────────────────────────────────────────
def move_jpg_files(source_folder: str, destination_folder: str) -> None:
    """
    Scans source_folder for .jpg / .jpeg files and moves them
    to destination_folder, creating it if it doesn't exist.
    """
    os.makedirs(destination_folder, exist_ok=True)

    moved = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpg", ".jpeg")):
            src  = os.path.join(source_folder, filename)
            dest = os.path.join(destination_folder, filename)
            shutil.move(src, dest)
            print(f"  Moved: {filename}")
            moved += 1

    print(f"  Done — {moved} file(s) moved to '{destination_folder}'.\n")


# ─────────────────────────────────────────────────────────────
# TASK 2 — Extract email addresses from a .txt file and save
# ─────────────────────────────────────────────────────────────
def extract_emails(input_file: str, output_file: str) -> None:
    """
    Reads input_file, finds every email address using a regex,
    deduplicates them, and writes the results to output_file.
    """
    email_pattern = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    emails = sorted(set(email_pattern.findall(text)))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(emails))
        f.write("\n")

    print(f"  Found {len(emails)} unique email(s). Saved to '{output_file}'.")
    for email in emails:
        print(f"    {email}")
    print()


# ──────────────────────────────────────────────────────────────
# TASK 3 — Scrape the <title> of a webpage and save it
# ──────────────────────────────────────────────────────────────
def scrape_page_title(url: str, output_file: str) -> None:
    """
    Fetches url, extracts the <title> tag content using re,
    and saves the result to output_file.
    Note: requests is imported here so the script still works
    even if requests is not installed when running Tasks 1 & 2.
    """
    try:
        import requests
    except ImportError:
        print("  'requests' library not installed. Run: pip install requests\n")
        return

    print(f"  Fetching: {url}")
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    title_match = re.search(r"<title[^>]*>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else "No <title> found"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"URL   : {url}\n")
        f.write(f"Title : {title}\n")

    print(f"  Title : {title}")
    print(f"  Saved to '{output_file}'.\n")


# ─────────────────────────────────────────────
# Demo / quick test
# ─────────────────────────────────────────────
if __name__ == "__main__":

    # ── Task 1 demo ──────────────────────────
    print("=== Task 1: Move .jpg files ===")
    os.makedirs("sample_images", exist_ok=True)
    # Create dummy .jpg files for the demo
    for name in ["photo1.jpg", "photo2.JPG", "notes.txt"]:
        open(os.path.join("sample_images", name), "w").close()

    move_jpg_files("sample_images", "jpg_output")

    # ── Task 2 demo ──────────────────────────
    print("=== Task 2: Extract emails ===")
    sample_text = (
        "Contact us at support@example.com or sales@company.org.\n"
        "You can also reach admin@test.io and duplicate@example.com.\n"
        "Invalid entries like @nouser or noatsign.com are ignored.\n"
        "Duplicate: support@example.com\n"
    )
    with open("sample_emails.txt", "w") as f:
        f.write(sample_text)

    extract_emails("sample_emails.txt", "extracted_emails.txt")

    # ── Task 3 demo ──────────────────────────
    print("=== Task 3: Scrape webpage title ===")
    scrape_page_title("https://example.com", "scraped_title.txt")
