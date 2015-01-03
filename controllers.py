from openerp.http import Controller, route, request


class Terminal(Controller):

    @route('/terminal/', auth="public")
    def index(self):
        return request.render('mrp_shopfloor_terminal.terminal_home') 
        #return "HOME"

#    @route('/terminal/details/<model("user"):.....', website=True, auth="user")
    @route('/terminal/details/', auth="public")
    def details(self):
        #user = request.env['user']
        #user = user.search([])
        return request.render('mrp_shopfloor_terminal.terminal_details')
 