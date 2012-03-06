IONUX.Models.DataResource = Backbone.Model.extend({

});

IONUX.Models.DataResourceDetails = Backbone.Model.extend({

  url: function(){
    return "/dataresource/"+this.get("data_resource_id")+"/";
  }

});


IONUX.Models.Observatory = Backbone.Model.extend({

  url: "/observatories/",
  idAttribute: "_id"

});

IONUX.Models.ObservatoryFacepageModel = Backbone.Model.extend({

  url: function(){
    return "/observatories/"+this.get("marine_facility_id")+"/";
  },
  
  parse: function(resp) {
    return resp.data;
  }

});


IONUX.Models.Platform = Backbone.Model.extend({

  url: "/platforms/",
  idAttribute: "_id"

});



IONUX.Models.PlatformFacepageModel = Backbone.Model.extend({

  url: function(){
    return "/platforms/"+this.get("platform_id")+"/";
  },
  
  parse: function(resp) {
    return resp.data;
  }

});


IONUX.Models.Instrument = Backbone.Model.extend({

  url: "/instruments/",
  idAttribute: "_id"

});


IONUX.Models.InstrumentFacepageModel = Backbone.Model.extend({

  url: function(){
    return "/instruments/"+this.get("instrument_id")+"/";
  },
  
  parse: function(resp) {
    return resp.data;
  }

});


IONUX.Models.ResourceType = Backbone.Model.extend({})
