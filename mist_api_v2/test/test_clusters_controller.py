import json
import time
import importlib

import pytest

from misttests.config import MIST_URL
from misttests.integration.api.helpers import assert_response_found
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']
REDIRECT_OPERATIONS = ['ssh', 'console']

resource_name = 'ClustersController'.replace('Controller', '').lower()
resource_name_singular = resource_name.strip('s')
try:
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{resource_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True
setup_data = {}


@pytest.fixture(autouse=True)
def after_test(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    test_operation = method_name.replace('test_', '')
    callback = setup_data.get(test_operation, {}).get('callback')
    if callable(callback):
        assert callback()
    else:
        sleep = setup_data.get(test_operation, {}).get('sleep')
        if sleep:
            time.sleep(sleep)


class TestClustersController:
    """ClustersController integration test stubs"""

    def test_create_cluster(self, pretty_print, owner_api_token):
        """Test case for create_cluster

        Create cluster
        """
        create_cluster_request = setup_data.get('create_cluster', {}).get(
            'request_body') or json.loads("""{
  "name" : "my-cluster",
  "provider" : "google",
  "location" : "europe-west2-b"
}""", strict=False)
        uri = MIST_URL + '/api/v2/clusters'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=create_cluster_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'create_cluster' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_destroy_cluster(self, pretty_print, owner_api_token):
        """Test case for destroy_cluster

        Destroy cluster
        """
        uri = MIST_URL + '/api/v2/clusters/{cluster}'.format(
            cluster=setup_data.get('destroy_cluster', {}).get('cluster') or setup_data.get('cluster') or 'my-cluster')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        if 'destroy_cluster' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_get_cluster(self, pretty_print, owner_api_token):
        """Test case for get_cluster

        Get cluster
        """
        query_string = setup_data.get('get_cluster', {}).get('query_string') or [('only', 'id'),
                        ('deref', 'auto'),
                        ('credentials', False)]
        uri = MIST_URL + '/api/v2/clusters/{cluster}'.format(
            cluster=setup_data.get('get_cluster', {}).get('cluster') or setup_data.get('cluster') or 'my-cluster')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'get_cluster' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_clusters(self, pretty_print, owner_api_token):
        """Test case for list_clusters

        List clusters
        """
        query_string = setup_data.get('list_clusters', {}).get('query_string') or [('cloud', '0194030499e74b02bdf68fa7130fb0b2'),
                        ('search', 'created_by:csk'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('deref', 'auto'),
                        ('at', '2021-07-21T17:32:28Z')]
        uri = MIST_URL + '/api/v2/clusters'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_clusters' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_scale_nodepool(self, pretty_print, owner_api_token):
        """Test case for scale_nodepool

        Scale cluster nodepool
        """
        scale_nodepool_request = setup_data.get('scale_nodepool', {}).get(
            'request_body') or json.loads("""{
  "desired_nodes" : 0,
  "max_nodes" : 1,
  "autoscaling" : true,
  "min_nodes" : 6
}""", strict=False)
        uri = MIST_URL + '/api/v2/clusters/{cluster}/nodepools/{nodepool}'.format(
            cluster=setup_data.get('scale_nodepool', {}).get('cluster') or setup_data.get('cluster') or 'my-cluster', nodepool=setup_data.get('scale_nodepool', {}).get('nodepool') or setup_data.get('nodepool') or 'my-nodepool-name')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=scale_nodepool_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'scale_nodepool' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')


if hasattr(_setup_module, 'TEST_METHOD_ORDERING'):
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestClustersController, method_name)
        setattr(TestClustersController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestClustersController):
        attr = getattr(TestClustersController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestClustersController, key, pytest.mark.order('last')(attr))

if SETUP_MODULE_EXISTS:
    # Add setup and teardown methods to test class
    class_setup_done = False

    @pytest.fixture(scope='class')
    def setup(owner_api_token):
        global class_setup_done
        if class_setup_done:
            yield
        else:
            global setup_data
            setup_data = _setup_module.setup(owner_api_token) or {}
            yield
            _setup_module.teardown(owner_api_token, setup_data)
            class_setup_done = True
    TestClustersController = pytest.mark.usefixtures('setup')(
        TestClustersController)
