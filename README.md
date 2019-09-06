# Shopping cart

It is a partial implementation of a shopping till system, which you might find at a supermarket.
This implementation was done by a Junior developer, you as a Senior Software Engineer have been requested to refactor this project.
You may make any technical decisions you would like, but must not change the given abstract class (abc.ShoppingCart) which is used by the shopping till hardware and cannot be easily updated.
Please treat this code as an element of a much larger production system which is being refactored for reliability and testability.

Tasks requested:
- Make the receipt print items in the order that they were added
- Add a 'Total' line to the receipt. This should be the full price we should charge the customer
- Be able to fetch product prices from an external source (json file, database ...)
- Be able to display the product prices in different currencies (not only Euro).
- Update the test suite to extend coverage and limit the number of tests which need changing when changes are introduced
- Any other changes which improve the reliability of this code in production

## Done
* Set up prices in json file and retrieve this in ShoppingCart object
* Set up helper function getCurr to retrieve currency rates relative to Euro from fixer.io api

## TODO
* Fix path accessing json file
* Change Test suite
  * granular tests testing one function
  * Test retrieving price data from json
    * check returned product, prices object is not empty
    * use these records in subsequent tests instead of hardcoding values
  * Test receiving currency data from api
    * Check api returned object is not empty
    * Add tests similar to existing tests but passing in required currency
    * Currency value to use in test can be retrieved from api database
  
