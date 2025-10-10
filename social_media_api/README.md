# Social Media API

A Django REST API for a social media platform with authentication, posts, comments, and more.

## Features
- User registration & login (Token-based authentication)
- User profile management
- Custom user model (bio, profile picture, followers)

## Setup
1. Clone the repo
2. Create and activate a virtual environment
3. Install dependencies
4. Run migrations and start server

## Endpoints
| Method | URL | Description |
|--------|-----|-------------|
| POST | /api/accounts/register/ | Register a new user |
| POST | /api/accounts/login/ | Login and get auth token |
| GET/PUT | /api/accounts/profile/ | View or edit profile |
