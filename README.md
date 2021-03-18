# Enrichr Vision

Enrichr is a python framework which sets out to address the security integration problem that vendors and analysts have. While the core functionality of Enrichr is targeted towards security enrichment, plugins are not limited to just enrichment. For example, plugins can push data, dispatch reporting jobs, add indicators to blacklists or other functionality.

There are 3 primary audiences for Enrichr:

- Security analysts
- Data Providers
- Security Integrators

## Security Analysts

Enrichr has a robust command line interface that can be used in day to day workflows. Enrichr provides a consistent method of interacting with many different vendor enrichments and provides a common workflow.

Additionally, since the framework is written in python and has sane defaults, analysts can use enrichr to automate either via bash scripts or simple python scripts.

## Data Providers

If you are a security vendor or provide data products, you no dobut realize how hard it can be to maintain integrations with dozens or hundreds of other products. Enrichr aims to alleviate those issues by providing a sane, tested framework that system integrators such as SIEM, SOAR and MSSP Providers can interface with third party products via a common interface.

Additionally, enrichr plugins are extremely flexible, so it is possible to expose advanced features and use enrichr as the primary API client for your customers to interact with your service.

## Security Integrators

Enrichr provides a high quality, standardized interface to a number of different security products that are supported by the community. This provides a rich ecosystem that integrators such as SOAR vendors, SIEM products and MSSPs can immediately utilize, so they can focus on their core areas of expertise rather than having to constantly worry about integrations.

### Official Plugins

Official plugins have rigorous standards that ensure integrators have a supported interface when interacting with different security products. These standards require that each plugin include things like unit tests, documentation, examples, packaging and continuous integration.

### Community Plugins

Plugins that do not meet the standards or are maintained by third parties are considered community plugins. While they still have standards that they conform to, these plugins might be missing things like unit tests, examples or comprehensive documentation.

## Repository and Module Structure

Enrichr splits each plugin into its own python module and repository. The main reason for this is a practical one, if there are third party dependencies that are required for a module to be supported, for example a yara or fuzzy hashing library that need to have C dependencies, enrichr shouldn't pull those in by default. Additionally, each plugin should be pushed to the Python Package Index through CI.
