/// <reference types="cypress" />
/// <reference types="@testing-library/cypress" />
describe('Landing page', function () {
  it('should navigate to the /test page', function () {
    cy.visit('/');

    cy.url().should('eq', Cypress.config().baseUrl + '/test');

    cy.findByRole('spinbutton', { name: /number/i }).should('exist');
    cy.findByRole('radio', { name: /get/i }).should('exist');
    cy.findByRole('radio', { name: /post/i }).should('exist');
    cy.findByRole('button', { name: /submit/i }).should('exist');
  });
});
