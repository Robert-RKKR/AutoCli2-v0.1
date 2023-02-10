GLOBAL_JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "AutoCli 2",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "AutoCli 2",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "AutoCli 2",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "ico/logo/RKKRlogo.svg",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "ico/favicon",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the AutoCli 2",

    # Copyright on the footer
    "copyright": "RKKR AutoCli 2",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "network", "logger"],

    # Custom icons for side menu apps/models
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "logger.Log": "fas fa-barcode",
        "logger.Extension": "fas fa-barcode",
        "data.PolicyTemplate": "fas fa-sticky-note",
        "data.PolicyTask": "fas fa-tasks",
        "data.PolicyRunner": "fas fa-tasks",
        "data.Policy": "fas fa-clipboard",
        "data.DeviceCollectedData": "fas fa-database",
        "data.DeviceUpdate": "fas fa-spinner",

        # System:
        "administration.Administrator": "fas fa-user",
        "settings.UserSetting": "fas fa-users-cog",
        "settings.Setting": "fas fa-users-cog",

        # Inventory:
        "inventory.Device": "fas fa-desktop",
        "inventory.DeviceType": "fas fa-keyboard",
        "inventory.DeviceTypeTemplate": "fas fa-sticky-note",
        "inventory.Group": "fas fa-users",
        "inventory.Credential": "fas fa-user-secret",

        # Messages:
        "logger.Log": "fas fa-barcode",
        "logger.Extension": "fas fa-barcode",
        "notifications.Notification": "fas fa-barcode",
        "changes.ChangeLog": "fas fa-barcode",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "order_with_respect_to": ["administration", "settings", "inventory", "notifications", "changes", "logger"],
}