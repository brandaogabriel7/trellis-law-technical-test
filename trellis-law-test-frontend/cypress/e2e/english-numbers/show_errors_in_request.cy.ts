/// <reference types="cypress" />
/// <reference types="@testing-library/cypress" />
describe('show errors in request', function () {
  beforeEach(function () {
    const errorResponse = {
      statusCode: 500,
      body: { status: 'error', error: 'This is an error message' },
    };
    cy.intercept(
      {
        method: 'GET',
        url: `${Cypress.env('apiUrl')}/num_in_english/*`,
      },
      errorResponse
    ).as('numInEnglishRequestGet');
    cy.intercept(
      {
        method: 'POST',
        url: `${Cypress.env('apiUrl')}/num_in_english/`,
      },
      errorResponse
    ).as('numInEnglishRequestPost');

    cy.visit('/test');

    cy.findByRole('spinbutton', { name: /number/i }).as('numberInput');
    cy.findByRole('radio', { name: /post/i }).as('postRadio');
    cy.findByRole('radio', { name: /get/i }).as('getRadio');
    cy.findByRole('button', { name: /submit/i }).as('submitButton');
  });

  it('should show numbers in english', function () {
    cy.get('@postRadio').click();

    cy.get('@numberInput').type('9999999999999');
    cy.get('@submitButton').click();
    cy.wait('@numInEnglishRequestPost');
    cy.findByText('This is an error message').should('exist');

    cy.get('@getRadio').click();
    cy.get('@submitButton').click();
    cy.wait('@numInEnglishRequestGet');
    cy.findByText('This is an error message').should('exist');
  });
});
