#
# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from oauth2client.service_account import ServiceAccountCredentials

import constants
from eclipse2017_exceptions import CouldNotObtainCredentialsError


def get_credentials(scopes=''):
    """
    Returns credentials object for eclipse service account or None.
    """
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            constants.SERVICE_ACCOUNT_PATH, scopes)
    except (IOError, ValueError, KeyError) as e:
        raise CouldNotObtainCredentialsError(e.message)
    return credentials
