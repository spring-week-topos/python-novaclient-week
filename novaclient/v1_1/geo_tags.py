# Copyright 2012 IBM Corp.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
GeoTags interface
"""
from novaclient import base


class GeoTag(base.Resource):
    def __repr__(self):
        return "<GeoTag: %s>" % self.server_name

    def _add_details(self, info):
        dico = 'resource' in info and info['resource'] or info
        for (k, v) in dico.items():
            setattr(self, k, v)


class GeoTagsManager(base.ManagerWithFind):
    resource_class = GeoTag
    
    def list(self, host=None):
        """
        List all available geo tags
        
        :param host: destination host name.
        """
        url = "/os-geo-tags"
        filters = []
        if host:
            filters.append("host=%s" % host)
        
        if filters:
            url = "%s?%s" % (url, "&".join(filters))
        return self._list(url, "geo_tags")

    def create(self, **kwargs):
        """Create a new GeoTag."""
        body = {'geo_tag': kwargs}
        return self._create('/os-geo-tags', body, 'geo_tag')
    
    def update(self, geo_tag_id,  **kwargs):
        """Update GeoTag.
        :param geo_tag_id Id of Geo Tag or compute host name
        """
        body = {'geo_tag': kwargs}
        return self._update('/os-geo-tags/%s' % geo_tag_id, body, 'geo_tag')
    
    def delete(self, geo_tag_id):
        """Delete GeoTag."""
        return self._delete('/os-geo-tags/%s' % geo_tag_id)
    
    def show(self, geo_tag_id):
        return self._get('/os-geo-tags/%s' % geo_tag_id, 'geo_tag')