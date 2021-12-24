describe('add user',()=>{
    it('to check add the user',()=>{
        cy.visit('localhost:3000')
        cy.findByRole('textbox', {
            name: /name/i
          }).type('Vignesh')
        cy.findByRole('spinbutton', {
        name: /age/i
        }).type(30)
        cy.findByRole('textbox', {
            name: /occupation/i
          }).type('LAMP Team Manager')
        cy.findByRole('button', {
        name: /submit/i
        }).click()
    })
}) 