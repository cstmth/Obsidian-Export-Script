#!/usr/bin/env python3

import os
import shutil
import re
import argparse

def copy_folder_structure(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f"✅ Copied folder: {src} → {dst}")

def find_used_images(source_paths):
    image_pattern = re.compile(r'!\[\[([^\]]+\.(?:png|jpg|jpeg))\]\]', re.IGNORECASE)
    used_images = set()

    for source_path in source_paths:
        for dirpath, _, filenames in os.walk(source_path):
            for filename in filenames:
                if filename.lower().endswith('.md'):
                    file_path = os.path.join(dirpath, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            matches = image_pattern.findall(content)
                            if matches:
                                print(f"🔍 Found images in {file_path}: {matches}")
                            used_images.update(matches)
                    except Exception as e:
                        print(f"⚠️ Could not read file {file_path}: {e}")
    return used_images

def copy_used_images(used_images, attachments_path, result_attachments_path):
    os.makedirs(result_attachments_path, exist_ok=True)
    for image in used_images:
        src_image = os.path.join(attachments_path, image)
        dst_image = os.path.join(result_attachments_path, image)
        if os.path.exists(src_image):
            shutil.copy2(src_image, dst_image)
            print(f"📦 Copied image: {image}")
        else:
            print(f"⚠️ Warning: Image not found: {image}")

def main():
    parser = argparse.ArgumentParser(
        description="📦 Export multiple folder subtrees from an Obsidian vault, including linked images."
    )
    parser.add_argument("vault_root", help="Path to the root of your Obsidian vault")
    parser.add_argument("attachments_folder", help="Relative path to the attachments folder (e.g., 'Ω Backend/Anhänge')")
    parser.add_argument("folders", nargs='+', help="One or more folders to export, followed by result folder")

    args = parser.parse_args()

    vault_root = os.path.abspath(args.vault_root)
    attachments_folder = args.attachments_folder
    *source_folders, result_root = args.folders
    result_root = os.path.abspath(result_root)

    attachments_path = os.path.join(vault_root, attachments_folder)
    result_attachments_path = os.path.join(result_root, attachments_folder)

    print(f"🚀 Starting export:")
    print(f"   Vault root:           {vault_root}")
    print(f"   Attachments folder:   {attachments_path}")
    print(f"   Result folder:        {result_root}")
    print(f"   Folders to export:    {source_folders}")

    source_paths = []
    for source_folder in source_folders:
        source_path = os.path.join(vault_root, source_folder)
        dst_source_path = os.path.join(result_root, source_folder)

        if not os.path.exists(source_path):
            print(f"❌ Source folder does not exist: {source_path}")
            continue

        copy_folder_structure(source_path, dst_source_path)
        source_paths.append(source_path)

    # Step 2: Find used images in all source folders
    used_images = find_used_images(source_paths)

    # Step 3: Copy used images
    copy_used_images(used_images, attachments_path, result_attachments_path)

    print("\n✅ Export completed!")

if __name__ == "__main__":
    main()

