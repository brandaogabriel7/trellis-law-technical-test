import num_english_responses from '../../fixtures/num_in_english/num_in_english_responses.json';

describe('POST num_in_english', function () {
  beforeEach(function () {
    cy.intercept(
      {
        method: 'POST',
        url: `${Cypress.env('apiUrl')}/num_in_english*`,
      },
      (req) => {
        const { number } = req.body;
        const response = num_english_responses[number];

        if (response) {
          req.reply({
            statusCode: 200,
            body: { status: 'ok', num_in_english: response },
            delay: 1000,
          });
        } else {
          req.reply(500, { status: 'error' });
        }
      }
    ).as('numInEnglishRequest');

    cy.visit('/test');

    cy.findByRole('spinbutton', { name: /number/i }).as('numberInput');
    cy.findByRole('radio', { name: /post/i }).as('postRadio');
    cy.findByRole('button', { name: /submit/i }).as('submitButton');
  });

  it('should show numbers in english', function () {
    cy.get('@postRadio').click();

    for (const [number, numInEnglish] of Object.entries(
      num_english_responses
    )) {
      cy.get('@numberInput').type(number);
      cy.get('@submitButton').click();
      cy.findByText(/loading/i).should('exist');
      cy.wait('@numInEnglishRequest');
      cy.findByText(numInEnglish).should('exist');
      cy.get('@numberInput').clear();
    }
  });
});
