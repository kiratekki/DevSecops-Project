### DevSecOps Security Pipeline

This project documents the process of building a secure DevSecOps CI/CD pipeline from the ground up. The goal is to simulate how modern engineering teams integrate security directly into the software development lifecycle rather than treating it as a final checkpoint.

The project starts with foundational concepts such as Linux security practices, Python scripting, and file permission analysis. These fundamentals form the base for automating tasks and understanding system-level security controls.

As the project progresses, a small web application will be developed and containerized using Docker. The pipeline will then integrate automated security testing tools such as Static Application Security Testing (SAST), Dynamic Application Security Testing (DAST), and container vulnerability scanning. The objective is to demonstrate how security checks can run automatically within a CI/CD workflow.

Automation will be implemented using GitHub Actions to create a pipeline that builds the application, runs security scans, and enforces security checks before deployment. The project will also explore secure deployment strategies in a cloud environment.

This repository will evolve over time. Each phase of the project will introduce new security tools, automation workflows, and defensive practices commonly used in real DevSecOps environments. By the end of the project, it will represent a complete example of a secure development pipeline that integrates application development, infrastructure automation, and security testing.


### Current Progress

Linux security fundamentals

Python scripting basics

File permission analysis and secure configuration practices

Planned Roadmap

Develop a simple web application

Containerize the application using Docker

Build a CI/CD pipeline using GitHub Actions

Integrate SAST security scanning

Integrate DAST testing

Implement container vulnerability scanning

Deploy the pipeline and application to a cloud environment


### Long-Term Goal

Create a fully functional secure DevSecOps pipeline that demonstrates practical security automation, suitable for portfolio demonstration and technical interviews.



### Known Vulnerabilities

During early testing of the application, several security weaknesses were identified. These findings are documented as part of the process of improving the security posture of the project while building the DevSecOps pipeline.

1. No Brute Force Protection

The login mechanism currently allows unlimited authentication attempts without any restriction.

# Risk
An attacker could repeatedly attempt different passwords until the correct one is discovered.

# Future Mitigation

Implement login rate limiting

Introduce account lockout after multiple failed attempts

Add CAPTCHA or multi-factor authentication

2. Information Disclosure

The login system currently returns a single generic message, “Credentials mismatch,” whenever authentication fails.

# Risk
Although this behavior is secure today, problems could arise if future updates introduce different error messages for invalid usernames and incorrect passwords. Distinct responses could allow attackers to identify valid usernames and focus password-guessing attacks on those accounts.

# Future Mitigation

Always return a single generic authentication failure message

Avoid revealing whether the username or password was incorrect

Maintain consistent error handling for all authentication failures

3. Lack of Input Validation

User input fields currently accept any data without validation or restrictions.

# Risk
Although the application currently does not use a database, unvalidated input could lead to security issues later if additional features are added (such as database queries or command execution).

# Future Mitigation

Implement input validation for username and password fields

Restrict unexpected characters and enforce length limits

Sanitize all user input before processing

## Security Improvement – Environment Variables for Credentials

Previously, the application stored login credentials directly inside the source code. 
This is considered an insecure design because sensitive information should never be 
hardcoded in source files that may be pushed to version control systems like GitHub.

### What was changed
The credentials were removed from the source code and are now stored in environment variables.

The application now reads credentials using environment variables such as:

- USERNAME
- PASSWORD

### Why this is more secure
- Prevents sensitive data from being exposed in the code repository
- Allows different credentials for different environments
- Follows security best practices used in DevSecOps workflows
- Protects secrets when sharing or publishing code

Environment variables are stored locally in a `.env` file which is ignored by Git.
