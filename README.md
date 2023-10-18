# Círculo de Crédito

## Arquitectura

El proyecto es completamente serverless construído con el [Serverless Framework](https://www.serverless.com/) y utilizando los servicios de AWS: [Lambda](https://aws.amazon.com/lambda/), [API Gateway](https://aws.amazon.com/api-gateway/) y [SQS](https://aws.amazon.com/sqs/).

La explicación a alto nivel de como están integrados estos servicos en conjunto se puede observar en la siguiente imagen. API Gateway expone un REST endpoint que funciona como el entry point a las Lambdas que realizan el trabajo de computación / lógica de negocio, y que a su vez interactúan con el servicio de Círculo de Crédito (CdC) y servicios de internos de Loft MX.

![High level overview](/assets/high-level-overview.png "High level overview")

El servicio de SQS lo utilizamos para poder procesar las peticiones del servicio de CdC de manera asíncrona y escalable, ya que estas pueden demorar hasta 60 segundos. La forma en la que tenemos configurada esta interacción está descrita en la siguiente imagen. Consiste en una Lambda con su respectivo entrypoint por medio de API Gateway la cual luego manda el mensaje a la cola de SQS de tipo FIFO (First In, First Out) para procesar las peticiones en orden, y que a su vez desencadena la Lambda que hace el procesamiento de la petición de CdC. Aunque es cierto que es posible hacer que el API Gateway llegue directo a la cola y poder así ahorrarnos una Lambda, usando el Serverless Framework esto es más complicado y engorroso en cuanto al código. Por esta razón optamos por tener una Lambda intermediaria.

![SQS high level overview](/assets/overview-sqs.png "SQS high level overview")

## Despliegue

El proyecto no tiene pipeline de CI/CD, por lo que el despliegue es manual usando el mismo serverless Framework. El comando básico de despliegue para el amiente de `staging` es:

```text
serverless deploy --aws-profile <aws_profile>
```

Donde `<aws_profile>` es un perfil de AWS previamente configurado en tu máquina local con todos los permisos necesarios para la cuenta correspondiente. Por defecto, el `stage` y la `region` ya están definidos para el ambiente de `staging`.

Para el despliegue al ambiente de `producción` es necesario indicar el `stage` y la `region` de manera explícita:

```text
serverless deploy --stage prod --region us-west-2 --aws-profile <aws_profile_prod>
```

## Despliegue Local

Para poder usar el proyecto de manera local se necesita tener `npm` instalado haber instalador la liberia de `serverless`
de manera local.

* Primero tienes que tener exportado el perfil  `aws` de manera local. 
```text 
    export AWS_PROFILE = perfil
```
* Segundo ejecutar `sls invoke -f {nombre de la funcion lambda dada de alta en serverless}`
```text 
    sls invoke -f  health_check
```
* Tercero en caso que se tenga que mandar a ejuctar un payload lo recomendable es hacer el archivo en raiz con extensión json y se ejecutaria de la siguiente manera `sls invoke -f {nombre de la funcion lambda dada de alta en serverless} -path  {ruta/nombre del archivo}` 

```text 
    sls invoke -f  health_check -p test/test.json
```


Nótese que los perfiles de AWS para cada ambiente son diferentes, ya que son cuentas separadas. **No uses el mismo perfil para desplegar a ambos ambientes**.

## Estructura de Carpetas

```plaintext
my-serverless-project/
├── src/
│   ├── application/
│   │   ├── use_cases/         # Casos de uso de la aplicación
│   │   ├── services/          # Servicios de aplicación
│   │   └── ...
│   ├── domain/
│   │   ├── entities/          # Entidades del dominio
│   │   ├── repositories/      # Interfaces de repositorios
│   │   ├── value_objects/     # Objetos de valor del dominio
│   │   └── ...
│   ├── infrastructure/
│   │   ├── data_sources/      # Implementaciones de repositorios (bases de datos, almacenamiento en caché, etc.)
│   │   ├── external/          # Integraciones externas (APIs, servicios en la nube, etc.)
│   │   └── ...
│   ├── interfaces/
│   │   ├── api/               # Controladores/API endpoints
│   │   └── ...
│   ├── main.py                # Punto de entrada principal
├── serverless.yml             # Configuración del servicio serverless
├── requirements.txt           # Dependencias del proyecto
├── .gitignore                 # Archivo de ignorar para Git

```

Explicación de las carpetas:

* `src/`: Esta es la carpeta principal donde reside el código fuente de tu aplicación.
* `application/`: Aquí se encuentran los casos de uso de tu aplicación y los servicios de aplicación. Los casos de uso representan las acciones específicas que tu aplicación puede realizar.
* `domain/`: Contiene las entidades del dominio, los objetos de valor y las interfaces de repositorios que definen las reglas de negocio y la lógica principal de tu aplicación.
* `infrastructure/`: Aquí colocas las implementaciones concretas de los repositorios y cualquier integración externa que tu aplicación necesite.
* `interfaces/`: Esta carpeta contiene los controladores/API endpoints que gestionan las solicitudes HTTP y la interacción con el exterior.
* `main.py`: El punto de entrada principal de tu aplicación serverless.
* `serverless.yml`: El archivo de configuración del servicio serverless que define las funciones Lambda, los eventos de disparo y otros recursos.
* `assets/`: Carpeta para guardar archivos relevantes a la documentación del proyecto.
* `requirements.txt`: Archivo que lista las dependencias de Python que necesita tu proyecto.
* `.gitignore`: Archivo para especificar qué archivos o carpetas deben ser ignorados por Git.

Esta estructura se centra en mantener una clara separación de preocupaciones y la independencia de la infraestructura, lo que facilita la prueba unitaria y la escalabilidad de tu proyecto serverless. Adaptarás el contenido de cada carpeta a las necesidades específicas de tu aplicación y la plataforma de servidor sin servidor que estés utilizando.

## Documentación Circulo de Credito

* **Documentación de Círculo de Crédito:** [Ver documentación](https://developer.circulodecredito.com.mx/apis)

* **Información de Suscripciones:** [Ver más](https://developer.circulodecredito.com.mx/suscripciones)

* **Guía de Webhooks en Suscripciones:** [Ir a la guía](https://developer.circulodecredito.com.mx/guia_de_suscripciones)

* **Información sobre EVA Simulación:** [Explorar producto](https://developer.circulodecredito.com.mx/producto/eva-simulacion)

## Solicitudes

## Descripción

Esta colección de solicitudes Postman proporciona una interfaz para interactuar con los servicios de Círculo de Crédito. Incluye solicitudes para consultar detalles de suscripciones, obtener información sobre prospectos, enviar información EVA y más.

## Uso

Siga estos pasos para utilizar la información y agregarla a Postman:

1. Configure las variables de entorno o las variables globales según sea necesario. Estas variables pueden incluir URL base, tokens de autenticación u otros datos específicos del entorno.

2. Explore y ejecute las diferentes solicitudes de la colección según sus necesidades. Cada solicitud incluye una descripción que explica su propósito y cómo debe configurarse.

### Suscripciones

#### Detalle de Suscripciones

* **Descripción:** Esta solicitud obtiene detalles de una suscripción específica.
* **Método:** GET
* **URL:** `https://1ie4wrhmtj.execute-api.us-east-1.amazonaws.com/suscription/ab04387b-a5ad-419c-92bc-04cbdcda43e1`
* **Ejemplo de respuesta:** [Ejemplo de respuesta aquí]

#### Lista de Suscripciones

* **Descripción:** Esta solicitud lista todas las suscripciones registradas en Círculo de Crédito.
* **Método:** GET
* **URL:** `https://1ie4wrhmtj.execute-api.us-east-1.amazonaws.com/suscriptions`
* **Ejemplo de respuesta:**

```json
{
    "subscriptions": [
        {
            "eventType": "mx.com.circulodecredito.eva",
            "webHookUrl": "https://1ie4wrhmtj.execute-api.us-east-1.amazonaws.com/webhook",
            "enrollmentId": "7ca4cebb-06ce-4549-b041-3e8879fdee09",
            "subscriptionId": "7c0f08e5-893e-4820-9923-91c8176d4a73",
            "dateTime": "2023-10-02T18:20:41Z"
        },
        {
            "eventType": "mx.com.circulodecredito.eva",
            "webHookUrl": "https://1ie4wrhmtj.execute-api.us-east-1.amazonaws.com/webhook",
            "enrollmentId": "214a868a-d9bb-44fe-938f-d9bd875ecabe",
            "subscriptionId": "f23c9bb5-c24c-49d0-aa4f-57ed0d728ade",
            "dateTime": "2023-10-02T19:06:12Z"
        },
        {
            "eventType": "mx.com.circulodecredito.eva",
            "webHookUrl": "https://1ie4wrhmtj.execute-api.us-east-1.amazonaws.com/webhook",
            "enrollmentId": "04ff0565-72a5-4e6a-ac85-6ec7b3a30b2c",
            "subscriptionId": "a9e2d39e-fb57-4235-a34c-05bb14bd5b2f",
            "dateTime": "2023-10-03T17:45:54Z"
        }
    ]
}

```

#### Usar Suscripción

* **Descripción:** Esta solicitud obtiene la suscripción actualizada para su uso en el payload de la solicitud de información del usuario.
* **Método:** GET
* **URL:** `https://1ie4wrhmtj.execute-api.us-east-1.amazonaws.com/suscription`
* **Ejemplo de respuesta:**

```json

{
    "uuid": "a9e2d39e-fb57-4235-a34c-05bb14bd5b2f",
    "created_at": "2023-10-03 17:45:55"
}
```

#### Publicar Información EVA

* **Descripción:** Esta solicitud envía información EVA a Círculo de Crédito para generar una solicitud de información del usuario.
* **Método:** POST
* **URL:** `https://1ie4wrhmtj.execute-api.us-east-1.amazonaws.com/create-eva-imss-authorization`
* **Cuerpo:**

```json
{
    "prospect_id": 1650,
    "issste": false,
    "privacyNotice": {
        "fullName": {
            "firstName": "Juan",
            "middleName": "string",
            "firstSurname": "Prueba",
            "secondSurname": "Prueba05",
            "aditionalSurname": "string"
        },
        "address": {
            "streetAndNumber": "HIDALGO 32",
            "settlement": "CENTRO",
            "county": "CUAUHTEMOC",
            "city": "CDMX",
            "state": "CDMX",
            "postalCode": "06000"
        },
        "acceptanceDate": "2020-04-12T22:20:50.52Z",
        "acceptance": "Y"
    },
    "employmentVerification": {
        "employmentVerificationRequestId": "d52892ff-7139-4ad2-893f-c615bfcb6b8e",
        "subscriptionId": "a9e2d39e-fb57-4235-a34c-05bb14bd5b2f",
        "curp": "PUPJ970229HDFZZG57",
        "email": "api57@circulodecredito.com.mx",
        "dataProvider": "ISS"

    }
}
```

* **Ejemplo de respuesta:**

```json

{
    "acknowledgeId": "316f2e83-c73a-467f-b8f2-29a3d065f8bb",
    "dateTime": "2023-10-03T22:52:09Z",
    "operation": "request",
    "message": "The employment verification request has been received.",
    "employmentVerificationRequestId": "d52892ff-7139-4ad2-893f-c615bfcb6b8e",
    "subscriptionId": "a9e2d39e-fb57-4235-a34c-05bb14bd5b2f",
    "inquiryId": "1b9507b5-f45d-4aad-9ee7-9c53f0ccb353"
}
```

#### Publicar Información ISSSTE

* **Descripción:** Esta solicitud envía información EVA a Círculo de Crédito para generar una solicitud de información del usuario de ISSSTE.
* **Método:** POST
* **URL:** `https://1ie4wrhmtj.execute-api.us-east-1.amazonaws.com/create-eva-issste-authorization`
* **Cuerpo:**

```json
{
    "prospect_id": 1650,
    "issste": true,
    "privacyNotice": {
        "fullName": {
            "firstName": "Juan",
            "middleName": "string",
            "firstSurname": "Prueba",
            "secondSurname": "Prueba05",
            "aditionalSurname": "string"
        },
        "address": {
            "streetAndNumber": "HIDALGO 32",
            "settlement": "CENTRO",
            "county": "CUAUHTEMOC",
            "city": "CDMX",
            "state": "CDMX",
            "postalCode": "06000"
        },
        "acceptanceDate": "2020-04-12T22:20:50.52Z",
        "acceptance": "Y"
    },
    "employmentVerification": {
        "employmentVerificationRequestId": "d52892ff-7139-4ad2-893f-c615bfcb6b8e",
        "subscriptionId": "a9e2d39e-fb57-4235-a34c-05bb14bd5b2f",
        "curp": "PUPJ970229HDFZZG57",
        "email": "api57@circulodecredito.com.mx",
        "dataProvider": "ISS"

    }
}
```

* **Ejemplo de respuesta:**

```json

{
    "acknowledgeId": "316f2e83-c73a-467f-b8f2-29a3d065f8bb",
    "dateTime": "2023-10-03T22:52:09Z",
    "operation": "request",
    "message": "The employment verification request has been received.",
    "employmentVerificationRequestId": "d52892ff-7139-4ad2-893f-c615bfcb6b8e",
    "subscriptionId": "a9e2d39e-fb57-4235-a34c-05bb14bd5b2f",
    "inquiryId": "1b9507b5-f45d-4aad-9ee7-9c53f0ccb353"
}
```

### Prospectos

#### Obtener Prospecto EVA

* **Descripción:** Esta solicitud obtiene información sobre un prospecto específico por su ID.

* **Método:** GET

* **URL:** `https://1ie4wrhmtj.execute-api.us-east-1.amazonaws.com/get-eva-prospect/1650`

* **Ejemplo de respuesta:**

```json
{
    "acknowledgeId": "316f2e83-c73a-467f-b8f2-29a3d065f8bb",
    "dateTime": "2023-10-03T22:52:09Z",
    "operation": "consume",
    "message": "The request has been consumed.",
    "employmentVerification": {
        {
            "employerName": "GPO DE DIS CONSTRN Y SUPERVISION, S.A. DE C.V.",
            "employerRegister": "Y622194810",
            "federalEntity": "DISTRITO FEDERAL",
            "startDate": "2002-02-04 00:00:00",
            "endDate": "2002-06-24 00:00:00",
            "lastContributionBaseSalary": 7466,
            "workStatusEvents": [
                {
                    "changeType": 2,
                    "eventDate": "2002-06-24 00:00:00",
                    "baseSalary": "7466"
                },
                {
                    "changeType": 8,
                    "eventDate": "2002-02-05 00:00:00",
                    "baseSalary": "7466"
                },
                {
                    "changeType": 8,
                    "eventDate": "2002-02-04 00:00:00",
                    "baseSalary": "7466"
                }
            ]
        }
    },
    "validUntil": "2019-12-03"
}
```

## Notas

* Estas peticiones las puedes agregar a postmal
* Revise las descripciones de cada solicitud para obtener más información sobre su uso.
