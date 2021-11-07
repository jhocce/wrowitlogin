import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleads import oauth2
# https://wrowit.herokuapp.com/google/redirect/

# Initialize the flow using the client ID and secret downloaded earlier.
# Note: You can use the GetAPIScope helper function to retrieve the
# appropriate scope for AdWords or Ad Manager.
flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
   client_secrets_file='client_secret.json',
    scopes=[oauth2.GetAPIScope('adwords')])
# Indicate where the API server will redirect the user after the user completes
# the authorization flow. The redirect URI is required.
flow.redirect_uri = 'https://wrowit.herokuapp.com/google/redirect/'
# Generate URL for request to Google's OAuth 2.0 server.
# Use kwargs to set optional request parameters.
authorization_url, state = flow.authorization_url(
# Enable offline access so that you can refresh an access token without
# re-prompting the user for permission. Recommended for web server apps.
access_type='offline',
# Enable incremental authorization. Recommended as a best practice.
include_granted_scopes='true')

print(authorization_url)

# https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=860637047 850-r79ahuck2ooqinta5ciqh55pm665qmgb.apps.googleusercontent.com&redirect_uri=htt ps%3A%2F%2Fwrowit.herokuapp.com%2F&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth %2Fadwords&state=uNTlqCeFI8e32451VPp3ebr2xbd5i8&access_type=offline&include_gran ted_scopes=true

# https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=558376713 536-hehho8pmk7lcbn7vumtmstikpjat85s6.apps.googleusercontent.com&redirect_uri=htt ps%3A%2F%2Fwrowit.herokuapp.com%2F&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth %2Fadwords&state=J6TV5Yqw8T2jvBnFc7coU8iXbYK2Pa&access_type=offline&include_gran ted_scopes=true

# https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=558376713536-hehho8pmk7lcbn7vumtmstikpjat85s6.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fwrowit.herokuapp.com%2Fgoogle%2Fredirect%2F&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fadwords&state=3VNJw3JUBAJDOL2Ho0DjWuBOtvb9qH&access_type=offline&include_granted_scopes=true