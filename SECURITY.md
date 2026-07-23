# Security Policy

## Supported version

Security fixes are applied to the latest commit on `main`.

## Reporting a vulnerability

Use GitHub's private security advisory feature for this repository. Do not open
a public issue containing credentials, student data, session details, or an
unpatched vulnerability.

Include:

- a concise description of the issue;
- affected file or workflow;
- steps to reproduce with fictional data;
- expected impact; and
- a suggested mitigation, if available.

## Credential and data handling

- Sign in to CCU systems manually inside Chrome.
- Never paste a password, one-time code, recovery code, or session token into
  an AI chat.
- Never commit browser profiles, cookies, downloaded student records, `.env`
  files, or agent-local configuration.
- Keep the Chrome debugging interface bound to `127.0.0.1`.
- Revoke exposed credentials before removing them from Git history.

## Scope

This project automates user-authorized browser workflows. It does not bypass
CAPTCHA, Cloudflare challenges, university access controls, or authorization
boundaries.
