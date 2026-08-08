# Gemini API — SKIPPED (known 403)

Per canonical spec §1.2-1.3 the Gemini API INT leg is a **known persistent 403**
and was intentionally NOT run in this POST-POLISH native-PDF round. This is a
documented infra limitation, not a review verdict. Gemini review coverage comes
from the EXT (headed-browser) sweep, not the API here.

- OpenAI native-PDF (gpt-5.5, Files API purpose=user_data + Responses input_file): RUN — 6/6 OK
- XAI/Grok native-PDF (grok-4.3, /v1/files upload + /v1/responses input_file): RUN — 6/6 OK
- Gemini API: SKIPPED (403), noted here.
