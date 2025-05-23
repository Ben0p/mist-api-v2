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

resource_name = 'MachinesController'.replace('Controller', '').lower()
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


class TestMachinesController:
    """MachinesController integration test stubs"""

    def test_associate_key(self, pretty_print, owner_api_token):
        """Test case for associate_key

        Associate a key with a machine
        """
        key_machine_association = setup_data.get('associate_key', {}).get(
            'request_body') or json.loads("""{
  "port" : 1,
  "machine" : "machine",
  "last_used" : 6,
  "sudo" : true,
  "user" : "user",
  "key" : "key"
}""", strict=False)
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/associate-key'.format(
            machine=setup_data.get('associate_key', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=key_machine_association)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        if 'associate_key' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_clone_machine(self, pretty_print, owner_api_token):
        """Test case for clone_machine

        Clone machine
        """
        query_string = setup_data.get('clone_machine', {}).get('query_string') or [('name', 'my-machine-clone'),
                        ('run_async', false)]
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/clone'.format(
            machine=setup_data.get('clone_machine', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'clone_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_console(self, pretty_print, owner_api_token):
        """Test case for console

        Open console
        """
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/console'.format(
            machine=setup_data.get('console', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'console' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_create_machine(self, pretty_print, owner_api_token):
        """Test case for create_machine

        Create machine
        """
        create_machine_request = setup_data.get('create_machine', {}).get(
            'request_body') or json.loads("""{
  "template" : "{}",
  "image" : "Debian",
  "quantity" : 5.962133916683182,
  "disks" : {
    "disk_size" : 0,
    "disk_path" : "disk_path"
  },
  "fqdn" : "fqdn",
  "cloudinit" : "cloudinit",
  "volumes" : "",
  "save" : true,
  "dry" : true,
  "monitoring" : true,
  "tags" : "{}",
  "cloud" : "cloud",
  "size" : "m1.small",
  "optimize" : "optimize",
  "schedules" : [ {
    "expires" : "2022-06-01 T00:00:00",
    "reminder" : {
      "message" : "message",
      "when" : {
        "unit" : "seconds",
        "value" : 6
      }
    },
    "name" : "backup-schedule",
    "description" : "Backup schedule",
    "run_immediately" : false,
    "selectors" : [ {
      "type" : "tags",
      "include" : [ "dev" ]
    } ],
    "actions" : [ {
      "action_type" : "start"
    } ],
    "when" : {
      "schedule_type" : "interval",
      "unit" : "minutes",
      "value" : 15
    },
    "enabled" : true
  }, {
    "expires" : "2022-06-01 T00:00:00",
    "reminder" : {
      "message" : "message",
      "when" : {
        "unit" : "seconds",
        "value" : 6
      }
    },
    "name" : "backup-schedule",
    "description" : "Backup schedule",
    "run_immediately" : false,
    "selectors" : [ {
      "type" : "tags",
      "include" : [ "dev" ]
    } ],
    "actions" : [ {
      "action_type" : "start"
    } ],
    "when" : {
      "schedule_type" : "interval",
      "unit" : "minutes",
      "value" : 15
    },
    "enabled" : true
  } ],
  "extra" : "",
  "name" : "DB mirror",
  "location" : "",
  "expiration" : {
    "date" : "2000-01-23T04:56:07.000+00:00",
    "action" : "stop",
    "notify" : {
      "period" : "minutes",
      "value" : 1
    },
    "notify_msg" : "notify_msg"
  },
  "net" : "",
  "scripts" : [ null, null ],
  "key" : ""
}""", strict=False)
        uri = MIST_URL + '/api/v2/machines'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=create_machine_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'create_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_destroy_machine(self, pretty_print, owner_api_token):
        """Test case for destroy_machine

        Destroy machine
        """
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/destroy'.format(
            machine=setup_data.get('destroy_machine', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'destroy_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_disassociate_key(self, pretty_print, owner_api_token):
        """Test case for disassociate_key

        Disassociate a key from a machine
        """
        key_machine_disassociation = setup_data.get('disassociate_key', {}).get(
            'request_body') or json.loads("""{
  "key" : "key"
}""", strict=False)
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/disassociate-key'.format(
            machine=setup_data.get('disassociate_key', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=key_machine_disassociation)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        if 'disassociate_key' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_edit_machine(self, pretty_print, owner_api_token):
        """Test case for edit_machine

        Edit machine
        """
        edit_machine_request = setup_data.get('edit_machine', {}).get(
            'request_body') or json.loads("""{
  "expiration" : {
    "date" : "date",
    "action" : "stop",
    "notify" : 0
  }
}""", strict=False)
        uri = MIST_URL + '/api/v2/machines/{machine}'.format(
            machine=setup_data.get('edit_machine', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=edit_machine_request)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        if 'edit_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_get_machine(self, pretty_print, owner_api_token):
        """Test case for get_machine

        Get machine
        """
        query_string = setup_data.get('get_machine', {}).get('query_string') or [('only', 'id'),
                        ('deref', 'auto')]
        uri = MIST_URL + '/api/v2/machines/{machine}'.format(
            machine=setup_data.get('get_machine', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'get_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_machines(self, pretty_print, owner_api_token):
        """Test case for list_machines

        List machines
        """
        query_string = setup_data.get('list_machines', {}).get('query_string') or [('cloud', '0194030499e74b02bdf68fa7130fb0b2'),
                        ('search', 'state:running'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('deref', 'auto'),
                        ('at', '2021-07-21T17:32:28Z')]
        uri = MIST_URL + '/api/v2/machines'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_machines' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_reboot_machine(self, pretty_print, owner_api_token):
        """Test case for reboot_machine

        Reboot machine
        """
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/reboot'.format(
            machine=setup_data.get('reboot_machine', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'reboot_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_rename_machine(self, pretty_print, owner_api_token):
        """Test case for rename_machine

        Rename machine
        """
        query_string = setup_data.get('rename_machine', {}).get('query_string') or [('name', 'my-renamed-machine')]
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/rename'.format(
            machine=setup_data.get('rename_machine', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'rename_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_resize_machine(self, pretty_print, owner_api_token):
        """Test case for resize_machine

        Resize machine
        """
        query_string = setup_data.get('resize_machine', {}).get('query_string') or [('size', '9417745961a84bffbf6419e5of68faa5')]
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/resize'.format(
            machine=setup_data.get('resize_machine', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'resize_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_resume_machine(self, pretty_print, owner_api_token):
        """Test case for resume_machine

        Resume machine
        """
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/resume'.format(
            machine=setup_data.get('resume_machine', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'resume_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_ssh(self, pretty_print, owner_api_token):
        """Test case for ssh

        Open secure shell
        """
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/ssh'.format(
            machine=setup_data.get('ssh', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'ssh' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_start_machine(self, pretty_print, owner_api_token):
        """Test case for start_machine

        Start machine
        """
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/start'.format(
            machine=setup_data.get('start_machine', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'start_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_stop_machine(self, pretty_print, owner_api_token):
        """Test case for stop_machine

        Stop machine
        """
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/stop'.format(
            machine=setup_data.get('stop_machine', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'stop_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_suspend_machine(self, pretty_print, owner_api_token):
        """Test case for suspend_machine

        Suspend machine
        """
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/suspend'.format(
            machine=setup_data.get('suspend_machine', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'suspend_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_undefine_machine(self, pretty_print, owner_api_token):
        """Test case for undefine_machine

        Undefine machine
        """
        query_string = setup_data.get('undefine_machine', {}).get('query_string') or [('delete_domain_image', True)]
        uri = MIST_URL + '/api/v2/machines/{machine}/actions/undefine'.format(
            machine=setup_data.get('undefine_machine', {}).get('machine') or setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'undefine_machine' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')


if hasattr(_setup_module, 'TEST_METHOD_ORDERING'):
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestMachinesController, method_name)
        setattr(TestMachinesController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestMachinesController):
        attr = getattr(TestMachinesController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestMachinesController, key, pytest.mark.order('last')(attr))

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
    TestMachinesController = pytest.mark.usefixtures('setup')(
        TestMachinesController)
