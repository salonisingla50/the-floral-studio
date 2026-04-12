import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thefloralstudio.settings')
django.setup()

from core.models import SiteSettings, NavLink, HeroSlide, Product, ProductCategory, SecondaryHero, Event, Footer

# Setup missing database links to the media files that already exist on the server

# 1. SiteSettings
SiteSettings.objects.get_or_create(id=1, defaults={
    'site_name': 'The Floral Studio', 
    'logo': 'logo/logo.jpg'
})

# 2. Hero Slides
HeroSlide.objects.get_or_create(headline='Discover Nature', defaults={
    'image': 'hero/green_wall.jpg', 
    'sub_text': 'Beautiful green walls', 
    'button_text': 'Shop Now', 
    'button_link': '/'
})
HeroSlide.objects.get_or_create(headline='Artificial Plants', defaults={
    'image': 'hero/artificial_plant_2.jpg', 
    'sub_text': 'Zero maintenance', 
    'button_text': 'Explore', 
    'button_link': '/'
})

# 3. Secondary Hero
SecondaryHero.objects.get_or_create(id=1, defaults={
    'image': 'secondary_hero/hero_background.webp', 
    'heading': 'Upgrade your space', 
    'sub_text': 'Find the perfect fit for your home.'
})

# 4. ProductCategory
cat, _ = ProductCategory.objects.get_or_create(name='Featured')

# 5. Products
Product.objects.get_or_create(name='Artificial Grass', defaults={
    'price': 49.99, 
    'image': 'products/artificial_grass_3.webp', 
    'description': 'Lush green grass'
})
Product.objects.get_or_create(name='Green Wall', defaults={
    'price': 120.00, 
    'image': 'products/green_wall.jpg', 
    'description': 'Vertical garden'
})

# 6. Events
Event.objects.get_or_create(title='Summer Collection', defaults={
    'image': 'events/summer_collection.jpg', 
    'description': 'Join us for our summer event.'
})

# 7. Nav Links
NavLink.objects.get_or_create(name='Home', defaults={'url': '/'})
NavLink.objects.get_or_create(name='Products', defaults={'url': '/products/'})

# 8. Footer (in case it wasn't successfully created)
Footer.objects.get_or_create(id=1)

print("Database seeded with existing media successfully!")
