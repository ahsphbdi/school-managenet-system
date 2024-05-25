FROM  lms_base_image:latest

# Ensure proper permissions for the application directories
RUN chown -R $APP_USER:$APP_USER $APP_HOME
RUN chmod -R 755 $APP_HOME

# Switch to the application user
USER $APP_USER

# copy dependency
COPY ./services/account/pyproject.toml  ./services/account/README.md $APP_HOME

# [OPTIONAL] Validate the project is properly configured
RUN poetry check

# Install Dependencies
RUN poetry install --no-interaction --no-cache

# copy source code
COPY ./services/account/accounts $APP_HOME/account/accounts/
COPY ./services/account/django_core $APP_HOME/account/django_core/
COPY ./services/account/utils $APP_HOME/account/utils/
COPY ./services/account/rest_api $APP_HOME/account/rest_api/
COPY ./services/account/permissions $APP_HOME/account/permissions/
COPY ./services/account/main.py $APP_HOME/account/main.py
COPY ./services/account/manage.py $APP_HOME/account/manage.py
COPY ./services/account/.env $APP_HOME/account/.env

# copy .pg_service.conf in user homepage
COPY ./services/account/.pg_service.conf $APP_HOME

# copy entrypoint.sh
COPY ./services/account/entrypoint.sh $APP_HOME
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# run entrypoint.sh
#ENTRYPOINT ["/home/python_user/entrypoint.sh"]

