#!/usr/bin/env bash
set -eou pipefail

# taken from the following article
# https://aws.amazon.com/blogs/containers/introducing-aws-copilot/
copilot_url="https://github.com/aws/copilot-cli/releases/download/v0.1.0/copilot-darwin-v0.1.0"
curl -Lo /usr/local/bin/copilot $copilot_url
chmod +x /usr/local/bin/copilot
