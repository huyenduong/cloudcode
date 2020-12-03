from azure.mgmt.compute import ComputeManagementClient
from azure.common.credentials import ServicePrincipalCredentials

# Authentication libraryy
from azure.identity import ClientSecretCredential

# Info for authenticationg
# Display name : huyeduon-restapi
# Application (client) ID : c4f505e2-b31b-42ad-8294-11991044cece
# Directory (tenant) ID : e34b6079-b8db-43a4-8104-4768856bd06c
# Object ID : 52a4d658-867e-41fa-947d-2f51befd0f2d

Subscription_Id="343fd6f5-2a74-4e53-95e3-d0766750dcc3"

tenant_id ="e34b6079-b8db-43a4-8104-4768856bd06c"
client_id="c4f505e2-b31b-42ad-8294-11991044cece"
client_secret="E9LpKrW-rqF7bRE3-2aMSML4Hq~-k.R.rw"

credential = ServicePrincipalCredentials(
        client_id=client_id,
        secret=client_secret,
        tenant=tenant_id
        )
compute_client = ComputeManagementClient(credential, Subscription_Id)


vm_list = compute_client.virtual_machines.list_all()
# vm_list = compute_client.virtual_machines.list('resource_group_name')
i= 0
for vm in vm_list:
    array = vm.id.split("/")
    resource_group = array[4]
    vm_name = array[-1]
    statuses = compute_client.virtual_machines.instance_view(resource_group, vm_name).statuses
    status = len(statuses) >= 2 and statuses[1]

    if status and status.code == 'PowerState/deallocated':
        print(vm_name)



