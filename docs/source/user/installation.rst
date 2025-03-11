Installation
============

The WMO CAP Composer can be installed in two ways:

1. As a standalone complete Wagtail project
2. As a set of Wagtail apps that can be integrated into an existing Wagtail project, such as `ClimWeb <climweb.readthedocs.io>`_.

Standalone Installation
-----------------------

This option will set up a Wagtail project together with the complete components required to run the WMO CAP Composer. Use this when
you want to use the WMO CAP Composer outside of an existing Wagtail project such as `ClimWeb <climweb.readthedocs.io>`_.

1. **Clone the repository**

   .. code-block:: shell

      git clone https://github.com/World-Meteorological-Organization/cap_composer.git

2. **Change into the project directory**

   .. code-block:: shell

      cd cap_composer

3. **Copy the sample environment file**

   .. code-block:: shell

      cp .env.standalone.sample .env

4. **Edit the `.env` file to set your environment variables.** See
   the `Standalone Environment Variables`_ below for more information. Use your favourite text editor to edit the file. For example, using `nano`:

   .. code-block:: shell

      nano .env

5. **Copy the nginx configuration file**

   .. code-block:: shell

      cp nginx/nginx.conf.sample nginx/nginx.conf

6. **Copy the docker-compose file**

   .. code-block:: shell

      cp docker-compose.sample.yml docker-compose.yml

7. **Build the Docker containers**

   .. code-block:: shell

      docker compose build

   This may take some time to download and build the required Docker images, depending on your internet connection.

8. **Run the Docker containers**

   .. code-block:: shell

      docker compose up -d

9. **Check the logs to ensure everything is running correctly**

   .. code-block:: shell

      docker compose logs -f

   In case of any errors, see the troubleshooting section below for some helpful
   tips: `Troubleshooting standalone installation`_

10. **Access the application at** ``http://<ip_or_domain>:<CAP_COMPOSER_WEB_PROXY_PORT>``. Replace ``<ip_or_domain>`` with the
    IP address or domain name of your server, and ``<CAP_COMPOSER_WEB_PROXY_PORT>`` with the port set in the `.env` file or `80`
    if not set.

11. **Create a superuser to access the admin dashboard**

    .. code-block:: shell

       docker compose exec cap_composer cap_composer createsuperuser

    ``cap_composer`` is a shortcut command to ``python manage.py`` in the Docker container.

12. **Access the admin dashboard at** ``http://<ip_or_domain>:<CAP_COMPOSER_WEB_PROXY_PORT>/<ADMIN_URL_PATH>``. Replace
    ``<ADMIN_URL_PATH>`` with the path set in the `.env` file or ``cap_composer-admin`` if not set.

Standalone Environment Variables
--------------------------------

**Note**: For a quick start, **5 environment variables are required**:

- **SECRET_KEY**
- **DB_PASSWORD**
- **REDIS_PASSWORD**
- **UID**
- **GID**

The rest are optional and can be configured as required.

.. list-table::
   :widths: 25 55 10 20
   :header-rows: 1

   * - Variable
     - Description
     - Required
     - Default
   * - SECRET_KEY
     - A unique secret key for securing your Django application. It’s used for encryption and signing. Do not share this key!
     - YES
     - (None)
   * - DB_PASSWORD
     - Password for cap_composer database
     - YES
     - (None)
   * - DB_USER
     - Username for cap_composer database
     - NO
     - cap_composer
   * - DB_NAME
     - Name of the cap_composer database
     - NO
     - cap_composer
   * - REDIS_PASSWORD
     - Password for cap_composer Redis Server
     - YES
     - (None)
   * - GUNICORN_NUM_OF_WORKERS
     - Number of workers for Gunicorn. Recommended value should be ``(2 x $num_cores) + 1``. Example: if your server has `4 CPU Cores`, set this to `9` (`(2 x 4) + 1 = 9`).
     - NO
     - 4
   * - CELERY_NUM_OF_WORKERS
     - Number of worker processes for Celery.
     - NO
     - 4
   * - DEBUG
     - A boolean that turns on/off debug mode. Never deploy a site into production with DEBUG turned on.
     - NO
     - False
   * - WAGTAIL_SITE_NAME
     - The human-readable name of your installation which welcomes users upon login to the Wagtail admin.
     - NO
     - cap_composer
   * - ADMIN_URL_PATH
     - Custom URL path for the admin dashboard. Should be one word and can include a hyphen. DO NOT include any slashes at the start or the end.
     - NO
     - cap_composer-admin
   * - TIME_ZONE
     - A string representing the time zone for this installation.
     - NO
     - UTC
   * - ALLOWED_HOSTS
     - A list of strings representing the host/domain names that this Django site can serve.
     - NO
     - 127.0.0.1,localhost

Important Notes
---------------

1. **Required Variables**: Ensure SECRET_KEY, DB_PASSWORD, and REDIS_PASSWORD are always set.
2. **Security**: Avoid using default values for sensitive variables like SECRET_KEY or ADMIN_URL_PATH.
3. **Debug Mode**: Never set DEBUG=True in production.
4. **Time Zone**: Set TIME_ZONE to your local time zone for accurate timestamps.
5. **SMTP**: Configure email settings if your app needs to send emails.

Troubleshooting standalone installation
---------------------------------------

1. **Docker containers not starting**: Check the logs for any errors. Run:

   .. code-block:: shell

      docker compose logs -f

2. **Docker compose file parsing errors**: Ensure the ``docker-compose.yml`` file is correctly formatted. Check for any
   syntax errors. Use:

   .. code-block:: shell

      docker compose config

   Some symbols like dollar signs ``($)`` or ``@`` might be causing issues in password variables, especially ``DB_PASSWORD``.

3. **Database volume permission errors**: Ensure the ``DB_VOLUME_PATH`` is correctly set and the database container user has the correct permissions. Assign permissions by running:

   .. code-block:: shell

      sudo chown -R 1000:1000 ./docker/volumes/db

4. **Static/media/backup volume permission errors**: Ensure ``STATIC_VOLUME_PATH``, ``MEDIA_VOLUME_PATH``, and ``BACKUP_VOLUME_PATH`` are correctly set. Set permissions using:

   .. code-block:: shell

      sudo chown -R <UID>:<GID> ./path/to/volume
