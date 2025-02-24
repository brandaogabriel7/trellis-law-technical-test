describe('Landing page', function () {
  it('should navigate to the /test page', function () {
    cy.visit('/');
    cy.url().should('eq', Cypress.config().baseUrl + '/test');
  });
});
