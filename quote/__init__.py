from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists

    # register the database commands

    from . import blog, user, api

    # register the blueprints
    app.register_blueprint(blog.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(api.bp)

    # db.init_app(app)

    # apply the blueprints to the app
    # make url_for('index') == url_for('blog.index')

    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app
