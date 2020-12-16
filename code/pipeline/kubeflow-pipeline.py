import kfp.dsl as dsl
from kubernetes.client.models import V1EnvFromSource, V1SecretKeySelector

@dsl.pipeline(
    name='Iris Classifcation',
    description='Iris Classification Problem'
)
def iris_classifier_train(imagetag='latest'):

    operations = {}

    # preprocess data
    operations['prepdata'] = dsl.ContainerOp(
        name='preprocess',
        image='kitchenregistry.azurecr.io/prepdata:' + str(imagetag)
    ).container.add_env_from(
        V1EnvFromSource(
            secret_ref=V1SecretKeySelector(
                name='github-access-token',
                key='GITHUB_ACCESS_TOKEN'))) # Needs to be a kubernetes secret in our namespace

    # train
    operations['training'] = dsl.ContainerOp(
        name='training',
        image='kitchenregistry.azurecr.io/train:' + str(imagetag)
    )
    operations['training'].after(operations['prepdata']).container.add_env_from(
        V1EnvFromSource(
            secret_ref=V1SecretKeySelector(
                name='github-access-token',
                key='GITHUB_ACCESS_TOKEN'))) # Needs to be a kubernetes secret in our namespace


    for _, op in operations.items():
        op.container.set_image_pull_policy("Always")


if __name__ == '__main__':
   import kfp.compiler as compiler
   compiler.Compiler().compile(iris_classifier_train, __file__ + '.tar.gz')
