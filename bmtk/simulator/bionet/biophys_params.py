import json
class BiophysParams(dict):
    def __init__(self, *args, **kwargs ):
        dict.__init__(self, *args, **kwargs )
        self._update_parameter_overrides()

    def _update_parameter_overrides(self):
        for key in self.keys():
            if key.startswith('genome.'):
                val = self.pop(key)
                self.update_nested(key, val)

    def get_nested(self, prop_string):
        group, section, name, mechanism = self._split_prop_string(prop_string)
        prop_records = [rec for rec in self[group] if rec['name']==name and rec['section']==section]
        if len(prop_records)==1:
            return prop_records[0]['value']
        elif len(prop_records)>1:
            raise ValueError('Multiple records found for dynamics parameter {}'.format(prop_string))
        else:
            raise ValueError('No records found for dynamics parameter {}'.format(prop_string))

    def update_nested(self, prop_string, value):
        group, section, name, mechanism = self._split_prop_string(prop_string)
        prop_records = [rec for rec in self[group] if rec['name']==name and rec['section']==section]
        if len(prop_records)==1:
            prop_records[0]['value'] = value
        elif len(prop_records)>1:
            raise ValueError('Multiple records found for dynamics parameter {}'.format(prop_string))
        elif mechanism:
            prop_record = {'section':section,
                            'name':name,
                            'value':value,
                            'mechanism':mechanism}
            self['genome'].append(prop_record)
        else:
            raise KeyError('Error updating dynamics parameter {}'.format(prop_string))

    @classmethod
    def from_json(cls, params_path):
        return cls(json.load(open(params_path, 'r')))

    @staticmethod
    def _split_prop_string(prop_string):
        path_list = prop_string.split('.')
        group, section, name = path_list[0:3]
        mechanism = path_list[-1] if len(path_list)==4 else None
        return group, section, name, mechanism