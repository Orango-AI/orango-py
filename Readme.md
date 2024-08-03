<p align="center">
  <img width="100" src="https://orango.ai/logo.svg" alt="Orango AI logo">
</p>

<h1 align="center">
  Orango Sandboxes
</h1>

<h3 align="center">
  Secure sandboxed cloud and edge environments made for AI agents and AI apps
</h3>

<h4 align="center">
  <a href="https://orango.ai/docs/">Docs</a> &#124;
  <a href="https://orango.ai">Website</a> &#124;
  <a href="https://orango-ai.slack.com">Slack</a> &#124;
  <a href="https://x.com/Orango_AI">Twitter</a>
</h4>

## What is Orango AI&#63;

Orango AI Sandbox is a secure sandboxed cloud environment made for AI agents and AI
apps. Sandboxes allow AI agents and apps to have long running cloud secure
environments. In these environments, large language models can use the same
tools as humans do. For example&#58;

- Cloud browsers
- GitHub repositories and CLIs
- Coding tools like linters, autocomplete, &quot;go-to defintion&quot;
- Running LLM generated code
- Audio &amp; video editing

**The Orango AI sandbox can be connected to any LLM and any AI agent or app.**

---

### Getting started &amp; documentation

&gt; Please visit [documentation](https://orango.ai/docs) to get started.

To create and control a sandbox, you use our SDK&#58;

## Installation

```sh
pip install orango
```

## Usage

```python
from orango import Sandbox

def run():
    sandbox = Sandbox.create(api_key='your-api-key-here', template_id='your-template-id-here')
    sandbox.exec('x = 1')

    execution = sandbox.exec('x += 1; x')
    print(execution['result'])  # outputs 2

    sandbox.close()

if __name__ == '__main__':
    run()
```

## Integration with LLM Frameworks

## SDKs

1. [JS SDK](https://www.npmjs.com/package/@orango-ai/sdk)
2. [Python](https://pypi.org/project/orango)
3. [CLI](https://www.npmjs.com/package/@orango-ai/cli)
4. [Documentation](https://orango.ai/docs/)

---

## Links

- [Support](mailto:hello@orango.ai)
- [Dashboard](https://orango.ai/dashboard)
- [API Reference](https://orango.ai/docs/api-reference)
- [Community](https://orango-ai.slack.com)
- [Blog](https://orango.ai/blog)

## Footer Socials

- [X (Twitter)](https://x.com/Orango_AI)
- [GitHub](https://github.com/Orango-AI)
- [LinkedIn](https://www.linkedin.com/company/orango-ai)

```

```
