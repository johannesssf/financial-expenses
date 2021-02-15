# Acceptance Tests

# Scenarios
1. [User Registration](#User_Registration)
1. [User Login](#User_Login)
1. [Categories](#Categories)
1. [Expenses Records](#Expenses_records)
1. [Expenses Dashboard](#Expenses_Dashboard)

## User Registration

Scenarios description

## User Login

Scenarios description

## Categories

**Scenario**: Create a new category

    Given I'm logged in
    And I'm at the categories page
    When I click on the "Add new" button
    And I fill in the category name and the target value
    And I click on the "Save" button
    Then I get a confirmation message
    And the new category is shown at the categories list

**Scenario**: Create a new category with an existing name

    Given I'm logged in
    And I'm at the categories page
    When I click on the "Add new" button
    And I fill in the category with an existing name and the target value
    And I click so save
    Then I get a message warning me what happened
    And I'm sent back to fill in a new category name

**Scenario**: Rename an existing category

    Given I'm logged in
    And I'm at the categories page
    When I click on the "Edit" button of a category
    And I rename the category
    And I click on the "Save" button
    Then the renamed category is shown on the categories list

**Scenario**: Delete a category

    Given I'm logged in
    And I'm at the categories page
    When I click on the "Delete" button of a category
    And I confirm the exclusion
    Then the category is removed from the categories list

**Scenario**: Delete an in use category

    Given I'm logged in
    And I'm at the categories page
    When I click on the "Delete" button of a category
    And I confirm to delete the category and all its records
    Then all records are deleted and the category is removed from the categories list

**Scenario**: Delete an in use category and move all its records to a different one

    Given I'm logged in
    And I'm at the categories page
    When I click on the "Delete" button of a category
    And I select a different category to move the records
    And I confirm the exclusion
    Then all records of the deleted category are moved to the new one and the selected category is removed from the categories list

## Expenses Records

Scenarios description

## Expenses Dashboard

Scenarios description


[Back](README.md)
