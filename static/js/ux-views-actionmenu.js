/*
Each View, Group, and Block element needs an action menu
that does many element-specfic actions based on a User's
selection for the element's corresponding Action Menu.


todo:
   - user triggering of some event ('hover'?), activated by 'main element hover', 
     to activate showing of action menu controls (that live in main elements 'header' element).
     * How do headers and elements know about each other?

*/

INTERACTIONS_OBJECT = {};
INTERACTIONS_OBJECT.block_interactions = ['More Info', 'Detailed View', 'Hide', 'Edit'];
INTERACTIONS_OBJECT.group_interactions = ['More Info', 'Detailed View', /*'Submenu',*/ 'Edit'];
INTERACTIONS_OBJECT.view_interactions = ['Subscribe', 'Detailed View', /*'Submenu',*/ 'Command', 'Direct Command', 'Download'];


IONUX.Views.ActionMenu = Backbone.View.extend({
    events:  {
        "click .dropdown-menu li": "action_control_click"
    },

    action_controls_onhover: function(evt){
        if (evt.type == 'mouseenter') {
            var btn = $(this.el).find(".btn-group");
            if (btn.length) {
                btn.show();
                return;
            }
        } 
        if (evt.type == 'mouseleave') {
            $(this.el).find(".btn-group").hide();
            return;
        }
        this.create_actionmenu();
    },

    create_actionmenu: function(){
        var dropdown_button_tmpl =
            '<div class="btn-group">'+
            '<a class="btn dropdown-toggle" data-toggle="dropdown" href="#">Actions<span class="caret"></span></a>'+
            '<ul class="dropdown-menu"><% _.each(dropdown_items, function(item) { %> <li><%= item %></li> <% }); %></ul>'+
            '</div>';
        var dropdown_items = INTERACTIONS_OBJECT.block_interactions; 
        var html = _.template(dropdown_button_tmpl, {"dropdown_items":this.interaction_items});
        $(this.el).prepend(html);
    },

    action_control_click: function(evt) {
        var action_name = $(evt.target).text();
        var action_event = "action__" + action_name.replace(/ /g, "_").toLowerCase()
        this.trigger(action_event);
    }

});


IONUX.Views.ViewActions = IONUX.Views.ActionMenu.extend({

    initialize: function() {
        this.interaction_items = INTERACTIONS_OBJECT.view_interactions;
        this.create_actionmenu();
        this.on("action__subscribe", this.action__subscribe);
        this.on("action__detailed_view", this.action__detailed_view);
        this.on("action__submenu_toggle", this.action__submenu_toggle);
        this.on("action__command", this.action__command);
        this.on("action__direct_command", this.action__direct_command);
        this.on("action__download", this.action__download);
    },
    action__subscribe:function(){
        var modal_html = '<div id="subscribe-modal" class="modal hide fade""></div>';
        $(modal_html).modal({keyboard:false})
            .on('shown', function(){
                new IONUX.Views.Subscribe().render().el;
            })
            .on('hidden',function(){
                $('#subscribe-modal').remove();
            });
    },
    action__detailed_view:function(){
        var modal_tmpl = '<div class="modal hide fade"><h1>Detailed View</h1><h3>Element: <%= elem_id %></h3></div>';
        var modal_html = _.template(modal_tmpl, {"elem_id":this.$el.attr("id")});
        $(modal_html).modal();
    },
    action__submenu_toggle:function(){
        alert("IONUX.Views.ViewActions - ACTION: submenu_toggle");
    },
    action__command:function(){
        var resource_type = window.MODEL_DATA['resource_type'];
        var resource_id = window.MODEL_DATA['_id'];
        if (resource_type == 'InstrumentDevice' || resource_type == 'PlatformDevice'){
            var router = new IONUX.Router();
            router.navigate('/'+resource_type+'/command/'+resource_id+'/', {trigger:true});
        } else {
            alert("Command not supported for " + resource_type + '.');
        };
    },
    action__direct_command:function(){
        alert("Direct Command");
    },
    action__download: function(evt){
        if (window.location.pathname.match(/DataProduct/g)){
            var url = get_descendant_properties(window.MODEL_DATA, $('#2164346').data('path'));
            window.open(url, '_blank');
        } else {
            alert("Download not available for this resource.");
        };
    },
});


IONUX.Views.GroupActions = IONUX.Views.ActionMenu.extend({

    "events": _.extend({
        "hover": "action_controls_onhover",
    }, IONUX.Views.ActionMenu.prototype.events),

    initialize: function() {
        this.interaction_items = INTERACTIONS_OBJECT.group_interactions;
        this.on("action__more_info", this.action__more_info);
        this.on("action__detailed_view", this.action__detailed_view);
        this.on("action__submenu_toggle", this.action__submenu_toggle);
        this.on("action__edit", this.action__edit);
    },

    action__more_info:function(){
        var modal_tmpl = '<div class="modal hide fade"><h1>More Info</h1><h3>Element: <%= elem_id %></h3></div>';
        var modal_html = _.template(modal_tmpl, {"elem_id":this.$el.attr("id")});
        $(modal_html).modal();
    },

    action__detailed_view:function(){
        alert("IONUX.Views.GroupActions - ACTION: detailed_view");
    },

    action__submenu_toggle:function(){
        alert("IONUX.Views.GroupActions - ACTION: submenu_toggle");
    },

    action__edit:function(){
        alert("IONUX.Views.GroupActions - ACTION: edit");
    }

});

IONUX.Views.BlockActions = IONUX.Views.ActionMenu.extend({

    "events": _.extend({
        "hover": "action_controls_onhover",
    }, IONUX.Views.ActionMenu.prototype.events),

    initialize: function() {
        this.interaction_items = INTERACTIONS_OBJECT.block_interactions;
        this.on("action__more_info", this.action__more_info);
        this.on("action__detailed_view", this.action__detailed_view);
        this.on("action__hide", this.action__hide);
        this.on("action__edit", this.action__edit);
    },

    action__more_info:function(){
        alert("IONUX.Views.BlockActions - ACTION: more_info");
    },
    action__detailed_view:function(){
        alert("IONUX.Views.BlockActions - ACTION: detailed_view");
    },
    action__hide:function(){
        alert("IONUX.Views.BlockActions - ACTION: hide");
    },
    action__edit:function(){
        alert("IONUX.Views.BlockActions - ACTION: edit");
    }

});


