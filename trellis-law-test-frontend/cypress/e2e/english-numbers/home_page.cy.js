describe('Navigating to the home page', function () {
  it('should navigate to home page', function () {
    cy.visit('/');
    cy.url().should('eq', Cypress.config().baseUrl + '/');
  });
});
