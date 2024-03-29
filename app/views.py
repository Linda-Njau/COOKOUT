from unicodedata import category
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Recipe, User
from .import db
import json
from flask_wtf import csrf

views = Blueprint('views', __name__)

@views.route('/about')
def about():
    """Returns about page"""
    return render_template('about.html')

@views.route('/')
def home():
    """Returns home page"""
    return render_template('index.html')

@views.route('/user/<username>')
@login_required
def user(username):
    """Returns user"""
    user = User.query.filter_by(username=username).first_or_404()
    recipes = Recipe.query.filter_by(user_id=user.id).all()
    return render_template('user.html', user=user, recipes=recipes)

@views.route('/new_recipe', methods=['GET', 'POST'])
@login_required
def new_recipe():
    """returns recipe creation page"""
    if request.method == 'POST':
        title = request.form.get('title')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instructions')
        preparation_time = request.form.get('preparation_time')
        cooking_time = request.form.get('cooking_time')
        calories = request.form.get('calories')
        servings = request.form.get('servings')
        hidden = bool(request.form.get('hidden'))
        collection_id = (request.form.get('collection_id'))
        
        if len(title) < 1:
            flash('Your recipe needs a title, wanna try again..?', category='error')
        else:
            new_recipe = Recipe(
                title=title,
                ingredients=ingredients,
                instructions=instructions,
                preparation_time=preparation_time,
                cooking_time=cooking_time,
                calories=calories,
                servings=servings,
                hidden=hidden,
                collection_id=collection_id,
                user_id=current_user.id
                )
            db.session.add(new_recipe)
            db.session.commit()
            flash('Your recipe is added!', category='success')
    return render_template("new_recipe.html", user=current_user)

@views.route('/my_recipes')
@login_required
def my_recipes():
    """displays a users recipes"""
    if current_user.is_authenticated:
        recipes = Recipe.query.filter_by(user_id=current_user.id).all()
        return render_template('my_recipes.html', recipes=recipes)
    else:
        return redirect(url_for('auth.signup'))

@views.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """allows user to edit profile"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        current_user.username = username
        current_user.email = email
        db.session.commit()
        flash('Profile updated successfully', category='success')
        return redirect(url_for('views.edit_profile'))
    return render_template('recipe.html', user=current_user, csrf_token=csrf.generate_csrf())

@views.route('/delete-recipe', methods=['POST'])
def delete_recipe():
    """Deletes a user's recipe"""
    recipe_id = request.form.get('recipeId')
    recipe = Recipe.query.get(recipe_id)
    
    if recipe and recipe.user_id == current_user.id:
        db.session.delete(recipe)
        db.session.commit()
    flash('Recipe deleted successfully.', category='success')
    return redirect(url_for('views.user_recipes'))

@views.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    """Follow functionality for the user"""
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found'.format(username), category='error')
        return redirect(url_for('home'))
    if user == current_user:
        flash('You cannot follow yourself!', category='error')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are now following {}'.format(username), category='success')
    return redirect(url_for('user', username=username))

@views.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    """unfollow functionality for the user"""
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found'.format(username), category='error')
        return redirect(url_for('home'))
    if user == current_user:
        flash('You cannot unfollow yourself!', category='error')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are no longer following {}.'.format(username), category='error')
    return redirect(url_for('user', username=username))
