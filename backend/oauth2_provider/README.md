# Autorizācija SKUDRA SERVER
Autorizācijai tiek izmanti oAuth2.0 principi.
Autorizācijai tiek izmants lietotāja vārds un parole, pamatā tiek izmantos AD lietotājs un parole, bet testa nolūkiem var izmantot Skudra server sistēmas lietotāju.

Lietotāja autorizācija notiek izmantots SKUDRA SERVER produkcijas serveris "https://skudra/" vai testēšanas un izstrādes nolūkiem "https://skudra-test/".

Autorizācijas, kā arī citu servisu  galapunkuts (endpoints) var iegūt no https://skudra/patrol/
```json
{
    "token_path": "/api/o/token/",
    "results_path": "/api/events/",
    "sample_path": "/api/events/samplespectra/?limit=1000",
    "remote_path": "/api/scheduler/units/",
    "licence_path": "/api/licenses/export/",
    ...
    "remote_units": "/api/scheduler/units/",
    "event_place_type": "/api/events/codif/place_type/",
    "authorization": "/api/o/token/"
}
```

## Autorizācija
Autorizācijai tiek izmantots "authorization" galapunkts.
```
POST /api/o/token HTTP/1.1
Host: https://skudra/
 
grant_type=password
&password={{password}}
&username={{username}}
&scope=read write groups
&client_id={{client_id}}
&client_secret={{client_secret}}
```

Katrai aplikācijai tiek izveidots savs client_id un client_secret

Pieprasījuma atbildē tiks saņemts autorizācijas un atjaunošanas atslēga, piemēram:
```json
{
    "access_token": "ZG1w3kSIKXxsHWermbGhsWkMw8HfqO",
    "expires_in": 604,
    "token_type": "Bearer",
    "scope": "read write groups",
    "refresh_token": "6pEcbx7z5y28VnvT0sUmx7lptjWg00"
}
```
## CSRF cookies
CSRF atslēgu ir iekspējams iegūt 2 galapunktos:
- https://skudra/patrol/
- https://skudra/api/config/default/

Cookie atselgās nosaukums: "csrftoken"
## Autorizētu pieprasījumu sutīšana
autorizētam Pieprasījuma sūtīšanai nepieciešams pievienot headera informāciju:
```
Authorization: Bearer {{token}}
```
kā arī pievienot  CSRF cookija atslēgu "csrftoken".

## Autorizācijas atslēgas atjaunošana

```
POST /api/o/token HTTP/1.1
Host: https://skudra/
 
grant_type=refresh_token
&refresh_token=refresh_token
&client_id=client_id
&client_secret=client_secret

```

Pēc pierpasījuma nosutīšanas, tika izdota jauna autorizācijas un atjaunošanas atslēga.