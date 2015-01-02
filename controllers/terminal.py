from openerp.http import Controller, route, request


class Terminal(Controller):

    @route('/terminal/', website=True, auth="user")
    def home(self):
        return request.render('mrp_shopfloor_terminal.terminal_home') 
    

#    @route('/terminal/details/<model("user"):.....', website=True, auth="user")
#    def details(self):
#        #user = request.env['user']
#        #user = user.search([])
#        return request.render('mrp_shopfloor_terminal.terminal_details')
 