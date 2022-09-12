# Copyright 2015-2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
#    http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under the License.

# locust-master: /bin/bash -c "exec /usr/local/bin/locust -f locustfile.py --master-port=9876 --master"
# locust-follower: /bin/bash -c "exec /usr/local/bin/locust -f locustfile.py --master-port=9876 --worker --master-host=$(<.masterIP)"

locust-master: /bin/bash -c "exec /usr/local/bin/locust -f ${LOCUSTFILE_NAME}"
# locust-follower: /bin/bash -c "exec /usr/local/bin/locust -f ${LOCUSTFILE_NAME} --worker --master-host=$(<.masterIP)"