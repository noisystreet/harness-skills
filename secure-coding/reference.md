# Secure Coding References

## Guides

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/) - common web risk classes.
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) - verification requirements by level.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) - practical controls for auth, injection, XSS, etc.
- [CWE Top 25](https://cwe.mitre.org/top25/) - recurring weakness types.
- [NIST SP 800-63](https://pages.nist.gov/800-63-3/) - digital identity guidance where relevant.

## What To Learn

- Validate at trust boundaries; authorize on the server.
- Treat secrets as unreadable in code, logs, and tickets.
- Prefer proven libraries for crypto; never invent protocols casually.

## Caveats

- Checklists do not replace threat modeling for high-risk systems.
- Language and framework defaults matter; follow project security baselines.
