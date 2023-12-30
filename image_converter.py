import os
from PIL import Image
import frontmatter

# Configuration
img_src_dir = 'imgsrc'  # Dossier source des images
posts_dir = '_posts'  # Dossier des posts Markdown
webp_dir = 'images'  # Dossier de destination pour les images WebP
max_width = 1280  # Largeur maximale des images
quality = 85  # Qualité des images WebP

print("*** Script de conversion des fichiers images en webp ***")


# Conversion des images en WebP seulement si nécessaire
for filename in os.listdir(img_src_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        base_name = os.path.splitext(filename)[0]
        webp_filename = base_name + '.webp'
        webp_path = os.path.join(webp_dir, webp_filename)

        # Vérifier si la conversion est nécessaire
        if not os.path.exists(webp_path):
            image_path = os.path.join(img_src_dir, filename)
            image = Image.open(image_path)
            
            # Redimensionnement si nécessaire
            if image.width > max_width:
                height = int(max_width * image.height / image.width)
                image = image.resize((max_width, height), Image.LANCZOS)

            # Enregistrement en WebP
            image.save(webp_path, 'WEBP', quality=quality)
            print(f"Image convertie : {webp_path}")

# Mise à jour et vérification dans les fichiers Markdown
for post_filename in os.listdir(posts_dir):
    if post_filename.lower().endswith(('.md', '.markdown')):
        post_path = os.path.join(posts_dir, post_filename)
        
        with open(post_path, 'r', encoding='utf-8') as file:
            post = frontmatter.load(file)
            content_changed = False

            # Vérifier et mettre à jour l'attribut 'image' dans le front matter
            if 'image' in post.metadata:
                image_name = post.metadata['image']
                image_extension = os.path.splitext(image_name)[1].lower()
                webp_image_name = os.path.splitext(image_name)[0] + '.webp'
                
                # Vérifier si on a un fichier avec vieux format... et si le nouveau existe le cas échéant le fichier WebP existe
                if image_extension in ['.jpg', '.jpeg', '.png'] and os.path.exists(os.path.join(webp_dir, webp_image_name)):
                    post.metadata['image'] = webp_image_name
                    content_changed = True

            # Mise à jour des liens d'images dans le contenu
            for old_image in os.listdir(img_src_dir):
                old_extension = os.path.splitext(old_image)[1]
                if old_extension in ['.jpg', '.jpeg', '.png']:
                    new_image = os.path.splitext(old_image)[0] + '.webp'
                    if new_image in os.listdir(webp_dir) and old_image in post.content:
                        post.content = post.content.replace(old_image, new_image)
                        content_changed = True

            # Sauvegarde si nécessaire
            if content_changed:
                with open(post_path, 'w', encoding='utf-8') as file:
                    file.write(frontmatter.dumps(post))
                print(f"Fichier Markdown mis à jour : {post_path}")

print("*** FIN Script de conversion des fichiers images en webp ***")
