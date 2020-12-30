from odps.udf import annotate
@annotate("*->string")
class ZipColumn():
    def evaluate(self,field1,field2,sep=',',k_v_sep=':',kv_sep=','):
        '''
        zip field1 and fileld2 to kv
        '''
        if field1 is None or field2 is None :
            return None

        field1s=field1.strip().split(sep)
        field2s=field2.strip().split(sep)
        if len(field1s) != len(field2s):
            raise "%s length is equal %s length"%(field1,field2)
        result=[]
        for k,v in zip(field1s,field2s):
            result.append(k+k_v_sep+v)
        return kv_sep.join(result)