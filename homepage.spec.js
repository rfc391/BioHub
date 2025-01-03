
describe('Frontend Tests', () => {
    it('Loads the homepage', () => {
        cy.visit('/');
        cy.contains('Welcome to BioHub').should('be.visible');
    });
});
