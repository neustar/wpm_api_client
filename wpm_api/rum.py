# Copyright 2000 - 2015 NeuStar, Inc.All rights reserved.
# NeuStar, the Neustar logo and related names and logos are registered
# trademarks, service marks or tradenames of NeuStar, Inc. All other
# product names, company names, marks, logos and symbols may be trademarks
# of their respective owners.
import urllib, json

class Rum:
    def __init__(self, connection, id):
        self.connection = connection
        self.id = id
        self.service = "/rum/1.0"
        
    def create(self, name):
        """Creates a new Real User web beacon and returns 'jsTag', the JavaScript tag that you should 
        copy and paste into your website's HTML header section.
        
        Arguments:
        name -- The name of this beacon.
        
        """
        new_beacon = {"beaconName": name}
        return self.connection.post(self.service + "/beacon", json.dumps(new_beacon))
        
    def list(self):
        """Retrieves a list of all RUM beacons associated with your account, along with information about
        each. The beacon id that is returned is used to make other api calls."""
        return self.connection.get(self.service + "/beacon")
        
    def update(self, **kwargs):
        """Change some or all of the preferences of an existing beacon. Requires the beacon ID retrieved 
        from the List Beacons api.
        
        Keyword Arguments:
        name -- The name of the beacon.
        max_load_time -- The maximum load time (ms) allowed per measurement.
        sampling_rate -- A number between 0 and 1 to represent the sampling rate for this beacon.
        
        """
        if self.id is None:
            raise Exception("Missing id: This API requires a rum beacon ID be supplied.")
        update_beacon = {}
        if "name" in kwargs:
            update_beacon.update({"beaconName": kwargs['name']})
        if "max_load_time" in kwargs:
            update_beacon.update({"maxLoadTime": kwargs['max_load_time']})
        if "sampling_rate" in kwargs:
            update_beacon.update({"samplingRate": kwargs['sampling_rate']})
        return self.connection.put(self.service + "/beacon/" + self.id, json.dumps(update_beacon))
        
    def delete(self):
        """Delete the given beacon. RUM data will no longer be collected for that beacon. Requires the 
        beacon ID retrieved from the List Beacons api."""
        if self.id is None:
            raise Exception("Missing id: This API requires a rum beacon ID be supplied.")
        return self.connection.delete(self.service + "/beacon/" + self.id)
        
    def data_summary(self, **kwargs):
        """Recent RUM data is aggregated to provide a short, easy to read summary.
        
        Keyword Arguments:
        minutes -- The number of minutes (between 1 and 60) to aggregate on. If this parameter is missing, 
                       the last 5 minutes worth of RUM data will be used to calculate the summary.
                       
        """
        params = {}
        if self.id is None:
            params.update({"allbeacons": 1})
        else:
            params.update({"beaconId": self.id})
        if "minutes" in kwargs:
            params.update({"minutes": kwargs['minutes']})
        return self.connection.get(self.service + "/data/summary", params)
        
    def data_recent(self, **kwargs):
        """Returns RUM's recently aggregated minute-level data.
        
        Keyword Arguments:
        minutes -- The number of minutes (between 1 and 60) to return. If this parameter is missing, the last 
                        5 minutes worth of RUM data will be returned.
                        
        """
        if self.id is None:
            raise Exception("Missing id: This API requires a rum beacon ID be supplied.")
        params = {"beaconId": self.id}
        if "minutes" in kwargs:
            params.update({"minutes": kwargs['minutes']})
        return self.connection.get(self.service + "/data/recent", params)
        
    def data_ts(self, start, end, **kwargs):
        """Returns RUM time series data for a given time period.
        
        Arguments:
        start -- An ISO 8601 formatted date string representing the start date in UTC from which you wish to 
                  retrieve time series data. Example: 2012-06-01T00:00:00Z
        end -- An ISO 8601 formatted date string representing the end date in UTC until which you wish to 
                 retrieve time series data. Example: 2012-06-05T00:00:00Z
                 
        Keyword Arguments:
        type -- If set to 'daily' this API will return day-level aggregated data. Otherwise this API will return 
                  minute-level aggregated data.
                  
        """
        if self.id is None:
            raise Exception("Missing id: This API requires a rum beacon ID be supplied.")
        params = {"beaconId": self.id, "startDate": urllib.quote_plus(start), "endDate": urllib.quote_plus(end)}
        if "type" in kwargs:
            params.update({"type": kwargs['type']})
        return self.connection.get(self.service + "/data/ts", params)
        
    def data_raw(self, start, end, **kwargs):
        """Returns samples from the raw data collected for a given time period. At a maximum, this api will return 
        2,000 samples. If there are more than 2,000 samples available for this time range, the 'more' field will be 
        set to true and you can make another api call specifying an offset which would be equal to the number of 
        results returned in the first api call plus the offset of that call. Only the last 7 days worth of raw data is 
        available.
        
        Arguments:
        start -- An ISO 8601 formatted date string representing the start date in UTC from which you wish to 
                  retrieve time series data. Example: 2012-06-01T00:00:00Z
        end -- An ISO 8601 formatted date string representing the end date in UTC until which you wish to 
                 retrieve time series data. Example: 2012-06-05T00:00:00Z
                 
        Keyword Arguments:
        offset -- From which position in the return list you wish to start. Default is 0.
        limit -- Specify a maximum number of results to return. Default (and max) is 2000.
        order_by -- Set this parameter to either 'asc' or 'desc' if you want the raw data returned either in 
                        ascending or descending order of page load time. If this parameter is not present, the 
                        default is to return the data in natural chronological order.
        errors_only -- Set this flag to 1 if you want results to only include samples that returned JavaScript 
                            errors.
        exact_url -- Filter raw samples by the exact url.
        url -- Filter raw samples by url using a regular expression.
        browser -- Filter raw samples by browser.
                           chrome
                           firefox
                           IE
                           android
        connection_type -- Filter raw samples by connection type.
                                        ocx
                                        tx
                                        dsl
                                        cable
                                        isdn
                                        mobile wireless
        country -- Filter raw samples by country.
        jserr -- Regex to filter raw samples by JS error filename or string.
        ipr -- Filter raw samples by IP Reputation Score: 
                   1 - Very Low Risk 
                   2 - Low Risk 
                   3 - Moderate Risk 
                   4 - High Risk 
                   5 - Very High Risk.
                   
        """
        if self.id is None:
            raise Exception("Missing id: This API requires a rum beacon ID be supplied.")
        params = {"beaconId": self.id, "startDate": urllib.quote_plus(start), "endDate": urllib.quote_plus(end)}
        if "offset" in kwargs:
            params.update({"offset": kwargs['offset']})
        if "limit" in kwargs:
            params.update({"limit": kwargs['limit']})
        if "order_by" in kwargs:
            params.update({"orderbypageloadtime": kwargs['order_by']})
        if "errors_only" in kwargs:
            params.update({"errorsonly": kwargs['errors_only']})
        if "exact_url" in kwargs:
            params.update({"urlexact": urllib.quote_plus(kwargs['exact_url'])})
        if "url" in kwargs:
            params.update({"url": urllib.quote_plus(kwargs['url'])})
        if "browser" in kwargs:
            params.update({"browser": kwargs['browser']})
        if "connection_type" in kwargs:
            params.update({"connection_type": kwargs['connection_type']})
        if "country" in kwargs:
            params.update({"country": urllib.quote_plus(kwargs['country'])})
        if "jserr" in kwargs:
            params.update({"jserr": urllib.quote_plus(kwargs['jserr'])})
        if "ipr" in kwargs:
            params.update({"ipr": kwargs['ipr']})
        return self.connection.get(self.service + "/data/raw", params)
        
    def data_analysis(self, start, end, **kwargs):
        """Returns RUM raw data filtered by the request parameters for a given time period, and grouped
        by a given key or over time. The maximum time period allowed is 24 hours as this API should be
        mostly used for alerting purposes.
        
        Arguments:
        start -- An ISO 8601 formatted date string representing the start date in UTC from which you wish to 
                  retrieve time series data. Example: 2012-06-01T00:00:00Z
        end -- An ISO 8601 formatted date string representing the end date in UTC until which you wish to 
                 retrieve time series data. Example: 2012-06-05T00:00:00Z
                 
        Keyword Arguments:
        group_by -- Key to group the data by. This parameter is required if the 'overtime' parameter is not set 
                          to 1.
        overtime -- Set this flag to 1 if you want results to be returned over time. If this flag is not set to 1 the 
                        'groupby' field becomes required. Note that this parameter is ignored when grouping by JS 
                        error.
        url -- Regex to filter raw samples by url. For example, in order to only retrieve measurements from a 
                .us domain we could use the string '.*\.us\/'
        browser -- Filter raw samples by browser.
                           chrome
                           firefox
                           IE
                           android
        connection_type -- Filter raw samples by connection type.
                                        ocx
                                        tx
                                        dsl
                                        cable
                                        isdn
                                        mobile wireless
        country -- Filter raw samples by country.
        jserr -- Regex to filter raw samples by JS error filename or string.
        ipr -- Filter raw samples by IP Reputation Score: 
                   1 - Very Low Risk 
                   2 - Low Risk 
                   3 - Moderate Risk 
                   4 - High Risk 
                   5 - Very High Risk.
                   
        """
        if self.id is None:
            raise Exception("Missing id: This API requires a rum beacon ID be supplied.")
        params = {"beaconId": self.id, "startDate": urllib.quote_plus(start), "endDate": urllib.quote_plus(end)}
        if "group_by" in kwargs:
            params.update({"groupby": kwargs['group_by']})
        if "overtime" in kwargs:
            params.update({"overtime": kwargs['overtime']})
        if "url" in kwargs:
            params.update({"url": urllib.quote_plus(kwargs['url'])})
        if "browser" in kwargs:
            params.update({"browser": kwargs['browser']})
        if "connection_type" in kwargs:
            params.update({"connection_type": kwargs['connection_type']})
        if "country" in kwargs:
            params.update({"country": urllib.quote_plus(kwargs['country'])})
        if "jserr" in kwargs:
            params.update({"jserr": urllib.quote_plus(kwargs['jserr'])})
        if "ipr" in kwargs:
            params.update({"ipr": kwargs['ipr']})
        return self.connection.get(self.service + "/data/analysis", params)
        
    def data_ol_ts(self, start, end):
        """Returns RUM Object-Level time series data for a given time period.
        
        Arguments:
        start -- An ISO 8601 formatted date string representing the start date in UTC from which you wish to 
                  retrieve time series data. Example: 2012-06-01T00:00:00Z
        end -- An ISO 8601 formatted date string representing the end date in UTC until which you wish to 
                 retrieve time series data. Example: 2012-06-05T00:00:00Z
                 
        """
        if self.id is None:
            raise Exception("Missing id: This API requires a rum beacon ID be supplied.")
        params = {"beaconId": self.id, "startDate": urllib.quote_plus(start), "endDate": urllib.quote_plus(end)}
        return self.connection.get(self.service + "/data/ol/ts", params)
        
    def data_ol_outlier(self, start, end, group_by):
        """Returns outlying page resources grouped by name, domain, and optionnally by location. The maximum
        time period allowed is 24 hours as this API should be mostly used for alerting purposes.
        
        Arguments:
        start -- An ISO 8601 formatted date string representing the start date in UTC from which you wish to 
                  retrieve time series data. Example: 2012-06-01T00:00:00Z
        end -- An ISO 8601 formatted date string representing the end date in UTC until which you wish to 
                 retrieve time series data. Example: 2012-06-05T00:00:00Z
        group_by -- Key to group the data by.
                              resource
                              domain
                              location_resource
                              location_domain
                              
        """
        if self.id is None:
            raise Exception("Missing id: This API requires a rum beacon ID be supplied.")
        params = {"beaconId": self.id, "startDate": urllib.quote_plus(start), "endDate": urllib.quote_plus(end), "groupby": group_by}
        return self.connection.get(self.service + "/data/ol/outlier", params)