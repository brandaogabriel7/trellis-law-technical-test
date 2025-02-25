import num_english_responses from '../../fixtures/num_in_english/num_in_english_responses.json';

describe('GET num_in_english', function () {
  beforeEach(function () {
    cy.intercept(
      {
        method: 'GET',
        url: `${Cypress.env('apiUrl')}/num_in_english*`,
      },
      (req) => {
        const { number } = req.query;
        const response = num_english_responses[number];
        if (response) {
          req.reply(200, { status: 'ok', num_in_english: response });
        } else {
          req.reply(500, { status: 'error' });
        }
      }
    ).as('numInEnglishRequest');

    cy.visit('/test');

    cy.findByRole('spinbutton', { name: /number/i }).as('numberInput');
    cy.findByRole('button', { name: /submit/i }).as('submitButton');
  });

  it('should show numbers in english', function () {
    for (const [number, numInEnglish] of Object.entries(
      num_english_responses
    )) {
      cy.get('@numberInput').type(number);
      cy.get('@submitButton').click();
      cy.wait('@numInEnglishRequest');
      cy.findByText(numInEnglish).should('exist');
      cy.get('@numberInput').clear();
    }
  });
});
