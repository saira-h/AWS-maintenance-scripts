# EC2Cleanup

This script cleans up AMIs and EC2s depending on a removal date in a "RemoveOn" tag that your resources must have. This will be in the format DD-MM-YYYY.
You can configure this to run as often as needed via timed CloudWatch event triggers on EventBridge.

## Usage

Change the regions and AWS Account number, and copy paste into Lambda console.
