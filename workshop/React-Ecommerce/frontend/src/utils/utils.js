export class Utils{
    convertToFormData(data){
        const formData = new FormData()
        Object.keys(data).forEach((key)=>{
            formData.append(key,data[key])
        })
        return formData;
    }
}

export const UtilService =  new Utils();